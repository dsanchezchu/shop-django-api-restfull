from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productsAll')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Product'
    
    def __str__(self):
        return self.name
    
    @property
    def category_name(self):
        return self.category.name
    