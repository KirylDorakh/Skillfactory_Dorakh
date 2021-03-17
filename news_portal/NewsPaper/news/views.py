from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, reverse, redirect

from django.core.mail import send_mail

from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Post, Author, Category, CategoryUser
from .filters import PostFilter, CategoryFilter
from .forms import PostForm, CategoryForm


class PostList(ListView):
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

        send_mail(
            subject=f'{subscribe.subscribers} {subscribe.name}',  # имя клиента и дата записи будут в теме для удобства
            message=f'Спасибо за подписку', # сообщение с кратким описанием проблемы
            from_email='kirill.dorokh@yandex.ru', # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=['kirill.dorokh@gmail.com',] # здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        return redirect('/news/subs_success')





