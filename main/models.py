from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer_Contract_From(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    img=models.ImageField( upload_to='product', verbose_name='Product Image',blank=True,null=True)
    name=models.CharField(verbose_name='Product Name' ,max_length=50)
    product_info=models.TextField(verbose_name='Product Information',blank=True,null=True)
    price=models.FloatField(verbose_name='Product Price')
    discaunt_price=models.FloatField(verbose_name='Product Discaunt Price',default=0.0,blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1,)
    
    def __str__(self):
        return f'{self.user.username}'
    
    def line_total(self):
        return self.product.price*self.quantity