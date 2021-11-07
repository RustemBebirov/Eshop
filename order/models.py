from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey
from product.models import Product
User = get_user_model()

# Create your models here.


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


