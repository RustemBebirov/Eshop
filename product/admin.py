from django.contrib import admin
from . models import Category,Product,Images
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

class ProdcutImagesInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','amount','image_tag','status',]
    list_filter = ['status','category','amount']
    inlines = [ProdcutImagesInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug':('title',)}

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ('image_tag',)





admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Images,ImagesAdmin)
