from django.contrib import admin
from .models import Settings,ContactUs
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    list_filter = ['status']

admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(Settings)
