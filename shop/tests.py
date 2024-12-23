from django.test import TestCase
from shop.models import Category, Products
# Realizar pruebas unitarias
class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name = "Test Category")
        Products.objects.create(name='Test Products', description='Test Description', price=100, category=Category.objects.get(name='Test Category'))
    
    def test_product_category_id(self):
        products=Products.objects.get(name='Test Products')
        self.assertEqual(products.category.id,1)

# Test de clases
class ProductsModelTest(TestCase):
    def setUp(self):
        category=Category.objects.create(name = "Teclados")
        Products.objects.create(name='Mouse g502', description='Test Description', price=100, category=category)
        Products.objects.create(name='Moude razer mamba v1.2',   description='Mouse gamer tope de gama', price=100, category=category)
        Products.objects.create(name='Moude razer mamba v1.2.1', description='Mouse gamer tope de gama', price=100, category=category)
    
    def test_product_list_view_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        
    # Listar los productos
    def test_product_list_view_query(self):
        response = self.client.get('/')
        # El response.context tiene que tener en los [' xxxx '] el mismo nombre que context_object_name en views
        self.assertEqual(len(response.context['products']),3)