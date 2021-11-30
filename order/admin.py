from django.contrib import admin
from .models import Order, OrderProduct, ShopCart
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','qty','amount']
    list_filter = ['user']


class OrderPrductLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','qty','amount','price')
    can_delete= False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','city','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','last_name',)
    inlines = [OrderPrductLine]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','qty','amount']
    list_filter = ['user']


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
admin.site.register(ShopCart,ShopCartAdmin)