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
# Create your tests here.
