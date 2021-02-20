from django.urls import path
from .views import ProductList, ProductDetail, Products

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
]