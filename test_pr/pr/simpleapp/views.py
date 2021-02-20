from django.views.generic import ListView, DetailView
from .models import Product

from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .filters import ProductFilter


class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')



class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта. в нём будет


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

