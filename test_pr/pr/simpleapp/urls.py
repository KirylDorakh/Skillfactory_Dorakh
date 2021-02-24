from django.urls import path
from .views import ProductList, ProductDetail, Products, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('', Products.as_view()),
    #path('<int:pk>', ProductDetail.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]