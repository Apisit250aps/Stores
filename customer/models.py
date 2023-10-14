from django.db import models
from django.contrib.auth.models import User 
from store.models import *

# Create your models here.

class CustomerData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    customer_code = models.CharField(max_length=8, unique=True)
    customer_contact = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_sub_district = models.CharField(max_length=128)
    customer_district = models.CharField(max_length=128)
    customer_province = models.CharField(max_length=128)
    customer_zip = models.CharField(max_length=5)
    customer_tel = models.CharField(max_length=10)
    customer_fax = models.CharField(max_length=10)
    customer_email = models.EmailField()
    customer_remark = models.TextField()
    
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.customer_code+" "+self.customer_contact
 
class OutputInvoice(models.Model):
    customer = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    
    invoice_no = models.CharField(max_length=10, unique=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    remark = models.TextField()
    
    output_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.invoice_no
    
class OutputData(models.Model):
    
    invoice = models.ForeignKey(OutputInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
   

    def __str__(self):
        
        return self.invoice.invoice_no+" "+self.product.product_name
    
