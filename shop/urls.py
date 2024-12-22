from django.urls import path
from .views import *
app_name = 'shop'
urlpatterns = [
    path('',index, name='index'),
    path('list',ProductList.as_view(), name='product_list'),
    path('<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path("product_form/", product_create, name="product_create")
]
