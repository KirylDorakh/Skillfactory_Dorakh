from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, AuthorList, CategoriesList, Subs, SubsSuccess, SubsUpdate, IndexView

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('add', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),

    path('authors', AuthorList.as_view()),

    path('categories', cache_page(300)(CategoriesList.as_view()), name='categories'),
    path('subs', Subs.as_view(), name='subs'),
    path('subs/<int:pk>/', SubsUpdate.as_view(), name='subs_update'),
    path('subs_success', SubsSuccess.as_view(), name='subs_success'),

    path('test_celery', IndexView.as_view()),

]