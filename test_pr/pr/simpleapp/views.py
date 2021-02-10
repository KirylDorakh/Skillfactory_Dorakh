from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта. в нём будет