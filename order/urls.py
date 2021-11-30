from django.urls import path
from order import views

app_name='order'

urlpatterns = [
    path('addtocart/<int:id>',views.addtocart, name='addtocart'),
    path('shopcart/',views.shopcart,name='shopcart'),
    path('deletecart/<int:id>/',views.deletetocart,name='deletecart')
]
