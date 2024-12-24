from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import CustomProductForm

class ProductList(ListView):
    model = Products
    template_name = "shop/product_list.html"
    context_object_name = 'products'


def index(request):
    categories = Category.objects.all()
    products = Products.objects.all()
    # Guardaremos en un diccionario
    context = {
        'categories' : categories,
        'products' : products
    }
    return render(request,'shop/index.html',context)

class ProductDetailView(DetailView):
    model = Products
    template_name = "shop/product_detail.html"
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Products
    form_class = CustomProductForm
    template_name = "shop/product_create.html"
    success_url = reverse_lazy('shop:product_list')