from django import forms
from .models import Products, Category

class CustomProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar cada campo con las clases de Tailwind
        self.fields['name'].widget.attrs.update({
            'class': 'border border-gray-300 w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Ingresa el nombre del producto'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'border border-gray-300 w-full px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Descripcion del producto',
            'rows': '2',
        })
        self.fields['price'].widget.attrs.update({
            'class': 'border border-gray-300 w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md',
            'placeholder': 'Ingresa el precio'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'id': 'categoria'
        })