from django import urls
from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('product-detail/<slug:slug>/',views.product_detail,name='product_detail'),
    path('category/<int:id>/<slug:slug>/',views.category_product,name='category_products'),
    path('search/',views.product_search,name='product_search'),
    path('filter/',views.filter,name='product_filter'),
    path('product_autocomplete/',views.product_autocomplete,name='product_autocomplete')
]

