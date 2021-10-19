from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Settings(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayir'),
    )
    title = models.CharField(max_length=127)
    keywords = models.CharField(max_length=127)
    description=models.CharField(max_length=255)
    company = models.CharField(max_length=127)
    address = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    fax = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    smtpserver = models.CharField(blank=True,max_length=127)
    smtpemail = models.CharField(blank=True,max_length=127)
    smtppassword = models.CharField(blank=True,max_length=127)
    smtpport = models.CharField(blank=True,max_length=127)
    icon = models.ImageField(blank=True,upload_to='icon_images/')
    facebook = models.CharField(blank=True,max_length=127)
    instagram = models.CharField(blank=True,max_length=127)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title



class ContactUs(models.Model):
    STATUS = (
        ('New','New'),
        ('Read',"Read"),
    )
    name = models.CharField(blank=True,max_length=50)
    email = models.EmailField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=127)
    phone = models.CharField(blank=True,max_length=127)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=15,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
        