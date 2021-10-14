from django import urls
from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('category/<int:id>/<slug:slug>/',views.category_product,name='category_products'),
    path('search/',views.product_search,name='product_search'),
    path('product_autocomplete/',views.product_autocomplete,name='product_autocomplete')
]

