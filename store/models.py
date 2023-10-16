from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductTypeData(models.Model):
    product_type = models.CharField(max_length=128, unique=True)
    product_type_code = models.CharField(max_length=8, unique=True, null=True)
    
    def __str__(self):
        return self.product_type
    
class ProductCategory(models.Model):
    product_type = models.ForeignKey(ProductTypeData, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=128)
    
    def __str__(self):
        return self.product_category
    
class ProductData(models.Model):
    product_code = models.CharField(max_length=8, unique=True, null=True)
    product_name = models.CharField(max_length=255)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

class ProductDelete(models.Model):
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
    
    delete_unit = models.IntegerField()
    delete_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_id.product_name
    


class AreaData(models.Model):
    area_name = models.CharField(max_length=128)
    area_code = models.CharField(max_length=4)
    
    def __str__(self):
        
        return self.area_name

class ShopData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductTypeData, on_delete=models.CASCADE)
    
    shop_code = models.CharField(max_length=8, unique=True, null=True)
    shop_name = models.CharField(max_length=128)
    shop_contact = models.CharField(max_length=255)
    shop_area = models.ForeignKey(AreaData, on_delete=models.CASCADE)
    shop_address = models.TextField()
    shop_sub_district = models.CharField(max_length=128)
    shop_district = models.CharField(max_length=128)
    shop_province = models.CharField(max_length=128)
    shop_zip = models.CharField(max_length=5)
    shop_tel = models.CharField(max_length=10)
    shop_fax = models.CharField(max_length=10)
    shop_email = models.EmailField()
    shop_remark = models.TextField()
    
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.shop_name


class InputInvoice(models.Model):
    shop = models.ForeignKey(ShopData, on_delete=models.CASCADE)
    
    invoice_no = models.CharField(max_length=10, unique=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    
    remark = models.TextField()
    input_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.invoice_no
    
class InputData(models.Model):
    
    invoice = models.ForeignKey(InputInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        
        return self.invoice.invoice_no+" "+self.product.product_name
    

    

    
    