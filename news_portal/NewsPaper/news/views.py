import logging

logger = logging.getLogger(__name__)

#для перевода
from django.utils.translation import gettext as _

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, reverse, redirect

from django.http import HttpResponse
from django.views import View
from .tasks import hello, printer, mailing
from datetime import datetime, timedelta, timezone

from django.core.mail import send_mail
from django.core.mail import mail_admins
from django.core.mail import mail_managers
from django.core.mail import EmailMultiAlternatives

from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.template.loader import render_to_string # импортируем функцию, которая срендерит наш html в текст

from .models import Post, Author, Category, CategoryUser
from .filters import PostFilter, CategoryFilter
from .forms import PostForm, CategoryForm

from django.core.cache import cache # импортируем наш кэш



class PostList(ListView):
    logger.error("Test!!")
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    # queryset = Post.objects.order_by('-id')
    ordering = ['-id']
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)  # кэш очень похож на словарь, и метод get действует также. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.get_queryset())
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj

class CategoriesList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'news/categories.html'
    context_object_name = 'news'
    ordering = ['-id']
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CategoryFilter(self.request.GET,
                                          queryset=self.get_queryset())
        context['form'] = CategoryForm()
        return context

    def post(self, request, *args, **kwargs):
        subs = Category(
            category=request.POST['name'],
            subscribers=request.user
        )
        subs.save()


class PostSearch(ListView):
    model = Post
    template_name = 'news/search_news.html'
    context_object_name = 'news'
    ordering = ['-id']
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                          queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    template_name = 'news/post_create.html'
    form_class = PostForm
    success_url = '/news/'


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news/post_update.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'


class Subs(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'subscribers/subscribe.html'
    context_object_name = 'categories'

    #def get(self, request, *args, **kwargs):
        #return render(request, 'subscribers/subscribe.html', {})

    def post(self, request, *args, **kwargs):
        subscribe = Category.objects.get(name=request.POST['category'])
        subscriber = self.request.user
        subscribe.subscribers.add(subscriber)
        subscribe.save()

        send_mail(
            subject=subscribe.name,
            message=f'hello {subscriber.username}',
            from_email='kyr.dor@mail.ru',
            recipient_list=[subscriber.email]
        )

        return redirect('/news/subs_success')

class SubsSuccess(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'subscribers/subs_success.html'
    context_object_name = 'categories'

class SubsUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'subscribers/subs_update.html'
    form_class = CategoryForm
    context_object_name = 'categories'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Category.objects.get(pk=id)

    def post(self, request, *args, **kwargs):
        subscribe = self.get_object()
        subscriber = self.request.user
        subscribe.subscribers.add(subscriber)
        subscribe.save()

        # получем наш html
        html_content = render_to_string(
            'subscribers/subscribe_created.html',
            {
                'subscribe': subscribe,
                'subscriber': subscriber,
            }
        )

        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        mail_admins(
            subject=f'{subscribe.name} {subscriber.username}',
            message=f'Подписка на {subscribe.name} от {subscriber.username}',
        )

        msg = EmailMultiAlternatives(
            subject=f'Подписка на {subscribe.name}',
            body=f'Спасибо, что подписались на {subscribe.name}, {subscriber.username}', #  это то же, что и message
            from_email='kyr.dor@mail.ru',
            to=[subscriber.email], # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html") # добавляем html

        msg.send() # отсылаем

        return redirect('/news/subs_success')


class IndexView(View):
    def get(self, request):
        printer.apply_async([10], eta = datetime.now(timezone.utc) + timedelta(seconds=5)) #eta = datetime.now(timezone.utc) + timedelta(seconds=5))
        # or datetime.utcnow()
        eta = datetime.now(timezone.utc) + timedelta(seconds=10)
        print(eta)
        hello.delay()
        return HttpResponse('Hello!')


class Index(View):
    def get(self, request, *args, **kwargs):
        if request.LANGUAGE_CODE == 'ru':
            string = _('Hello world')

            return HttpResponse(string)
        else:
            return HttpResponse("You prefer to read another language.")





