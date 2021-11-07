from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayir'),
    )
    title = models.CharField(max_length=127)
    keywords = models.CharField(max_length=127)
    description=models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='product_images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self) -> str:
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayir'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    keywords = models.CharField(max_length=127)
    description=models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='product_images/')
    status = models.CharField(max_length=10,choices=STATUS)
    price = models.FloatField()
    sale = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail',args=([self.slug]))
    

class Images(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')
    title = models.CharField(max_length=127,blank=True,null=True)
    image = models.ImageField(blank=True,upload_to='images/')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'{self.product} ,{self.title}'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

