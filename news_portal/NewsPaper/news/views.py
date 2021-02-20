from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostSearch(ListView):
    model = Post
    template_name = 'search_news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                          queryset=self.get_queryset())
        return context