from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Customer_Contract_From(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    message=models.TextField()
    
    def __str__(self):
        return self.name
STOCK_PRODUCT=(('In Stock','In Stock'),
               ('Stock Out','Stock Out')
               
)
class Product(models.Model):
    
    img=models.ImageField( upload_to='product', verbose_name='Product Image',blank=True,null=True)
    name=models.CharField(verbose_name='Product Name' ,max_length=50)
    product_info=models.TextField(verbose_name='Product Information',blank=True,null=True)
    price=models.FloatField(verbose_name='Product Price')
    discaunt_price=models.FloatField(verbose_name='Product Discaunt Price',default=0.0,blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    abability=models.CharField(choices=STOCK_PRODUCT, max_length=50,blank=True,null=True)
    
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
    
class Coupon(models.Model):
    code = models.CharField( max_length=50,unique=True)
    valid_date=models.DateField() 
    valid_form=models.DateField()  
    discaunt=models.FloatField()
    active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.code

ORDER_STATUS=(
    ('Procecing','Procecing'),
    ('Order Accept','Order Accept'),
    ('Run the way','Run the way'),
    ('Dalivared','Dalivared')
)
class OrderPlace(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    country=models.CharField( max_length=50,blank=True,null=True)
    first_name=models.CharField( max_length=50,blank=True,null=True) 
    last_name=models.CharField( max_length=50,blank=True,null=True)
    company_name=models.CharField( max_length=50,blank=True,null=True)
    addess=models.CharField( max_length=50,blank=True,null=True)
    aperment=models.CharField( max_length=50,blank=True,null=True)
    state=models.CharField( max_length=50,blank=True,null=True)
    zip=models.CharField( max_length=50,blank=True,null=True)
    email=models.EmailField( max_length=50,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    note=models.TextField(blank=True,null=True)
    status=models.CharField(choices=ORDER_STATUS, max_length=50,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user.username}'
    
    
    
class OurTeam(models.Model):
    name=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    description=models.TextField()
    img=models.ImageField(upload_to='team' )
    
    def __str__(self):
        return self.name
    