from django.urls import path
from .views import PostsList, PostDetail, PostsFilter, PostAddView, PostDeleteView, PostEditView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', PostsFilter.as_view()),
    path('add/', PostAddView.as_view(), name='post_add'),  # Ссылка на создание товара
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Ссылка на удаление
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),  # Ссылка на создание
]
