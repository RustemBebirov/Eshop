from django.forms import ModelForm, fields
from .models import ShopCart


class ShopCartForm(ModelForm):

    class Meta:
        model = ShopCart
        fields = ['qty']

