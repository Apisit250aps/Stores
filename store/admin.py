from django.contrib import admin


from . import models

# Register your models here.

@admin.register(models.AreaData)
class AreaDataAdmin(admin.ModelAdmin):
    list_display = [
        'area_code',
        'area_name'
    ]
    
@admin.register(models.ShopData)
class ShopDataAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'shop_code',
        'shop_name',
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
    
@admin.register(models.ProductData)
class ProductDataAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
    ]

@admin.register(models.InputInvoice)
class InputInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'invoice_no',
        
    ]

@admin.register(models.InputData)
class InputDataAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'invoice'
    ]