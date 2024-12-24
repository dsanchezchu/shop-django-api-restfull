from django import forms
from .models import Products, Category

class CustomProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category','image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mejora el diseño de cada campo con las clases de Tailwind
        self.fields['name'].widget.attrs.update({
            'class': 'border border-gray-300 w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Ingresa el nombre del producto',
            'style': {'font-size': '16px'}
        })
        self.fields['description'].widget.attrs.update({
            'class': 'border border-gray-300 w-full px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Descripcion del producto',
            'rows': '3',
            'style': {'font-size': '16px'}
        })
        self.fields['price'].widget.attrs.update({
            'class': 'border border-gray-300 w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Ingresa el precio',
            'style': {'font-size': '16px'}
        })
        self.fields['category'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'id': 'categoria',
            'style': {'font-size': '16px'}
        })
        self.fields['image'].widget.attrs.update({
            'class': 'border border-gray-300 w-full px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Ingresa la URL de la imagen',
            'style': {'font-size': '16px'},
            'accept': 'image/*'
        })