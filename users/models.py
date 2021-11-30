from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your models here.

class User(AbstractUser):

    email = models.EmailField('Email',unique=True)
    image = models.ImageField("Image 40x40 ",upload_to='profile_images',null=True,blank=True, default='profile.jpg')
    phone = models.CharField("Phone",max_length=50, unique=True,null=True,blank=True)
    country = models.CharField("Country",max_length=127,null=True,blank=True)
    city = models.CharField("City",max_length=127,null=True,blank=True)
    address = models.CharField("Address",max_length=127,null=True,blank=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.email

    