from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, AuthorList, CategoriesList

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('add', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),

    path('authors', AuthorList.as_view()),

    path('categories', CategoriesList.as_view(), name='categories'),

]