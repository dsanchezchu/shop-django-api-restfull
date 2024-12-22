from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from .models import *

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

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        category = Category.objects.get(id=category)
        products = Products.objects.create(
            name=name,
            description=description,
            price=price,
            category=category
        )
        return redirect('shop:product_detail', pk=products.id)
    context = {
        'categories' : Category.objects.all()
    }
    return render(request,'shop/product_create.html',context)