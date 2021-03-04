from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
# импортируем класс, который говорит нам о том, что в этом представлении
# мы будем выводить список объектов из БД
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .models import Post, Author
from .filters import PostFilter, PostFilterView  # импортируем недавно написанный фильтр
from .forms import PostForm, AuthorForm
from django.contrib.auth.mixins import PermissionRequiredMixin


# создаём представление в котором будет детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона
    context_object_name = 'new'  # название объекта в нём будет


class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    queryset = Post.objects.order_by('-id')
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать html,
    # в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты,

    # его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные.
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    paginate_by = 10  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['filter'] = PostFilterView(self.request.GET, queryset=self.get_queryset())
        return context


class PostsFilter(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')
    template_name = 'search.html'
    context_object_name = 'news'
    # ordering = ['-date_post']
    paginate_by = 5  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data
        # у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class PostAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', )
    template_name = 'news/post_add.html'
    form_class = PostForm
    success_url = '/news/'


# дженерик для редактирования объекта
class PostEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news/post_edit.html'
    form_class = PostForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset,
    # чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

    # метод get_object мы используем вместо queryset,
    # чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


