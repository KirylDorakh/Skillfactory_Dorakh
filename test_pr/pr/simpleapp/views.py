from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm


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
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/products/'


class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/products/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
