from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from product.models import Product
from django.forms import ModelForm
User = get_user_model()

# Create your models here.


class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Preparing','Preparing'),
        ('Onshipping','Onshipping'),
        ('Completed','Completed'),
        ("Canceled",'Canceled'),
    )

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    address = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    country = models.CharField(max_length=127)
    ip = models.CharField(max_length=127)
    status = models.CharField(max_length=15,choices=STATUS,default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['ip','status','created_at','updated_at']


class OrderProduct(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ("Canceled",'Canceled'),
    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()
    amount = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS, default='New')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product.title


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()

    def __str__(self) -> str:
        return self.product.title

    @property
    def amount(self):
        return (self.qty * self.product.price)

    @property
    def price(self):
        return (self.product.price)


