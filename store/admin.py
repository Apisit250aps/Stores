from django.contrib import admin


from . import models

# Register your models here.

@admin.register(models.AreaData)
class AreaDataAdmin(admin.ModelAdmin):
    list_display = [
        'area_code',
        'area_name'
    ]
    
@admin.register(models.ProductTypeData)
class ProductTypeDataAdmin(admin.ModelAdmin):
    list_display = [
        'product_type',
        'product_type_code'
    ]
    
@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'product_category',
        'product_type',
    ]
    