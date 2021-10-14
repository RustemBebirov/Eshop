from django.contrib import admin
from django.contrib.auth import get_user_model

User=get_user_model()
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(User,UserAdmin)