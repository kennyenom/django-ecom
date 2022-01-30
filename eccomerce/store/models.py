from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

# Create your models here.

STATE_CHOICES =(
    ('nairobi','nairobi'),
    ('ruiru','ruiru'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(choices=STATE_CHOICES,max_length=50,null=True)

    def __str__(self):
        return str(self.id)
class Category(models.Model):
    title= models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='cat_imgs',null=True)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=200,null=True)
    selling_price = models.FloatField(null=True)
    price = models.FloatField(null=True,blank=False)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=100,null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True)
    product_image=models.ImageField(upload_to='product-imgs/',null=True)


    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True)


    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.price
    

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','on The Way'),
    ('Delivered','delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    staus = models.CharField(choices=STATUS_CHOICES,default='Pending',max_length=40,null=True)
    



