from . import models

def ShopCode(product_type:int, area:int, shop_id:int):
    
    return f"{int(product_type)*10}{int(area)*10}{1000+int(shop_id)}"

def InvoiceNo(shop_code:str, invoice_id:int):
    
    return f"{shop_code[-4::]}{1000+int(invoice_id)}"

def ProductCode(shop_id, product_id):
    
    return str(int(shop_id)*10000+int(product_id))


def ProductCategory(category, types: int):
    type = models.ProductTypeData.objects.get(id=types)
    try:
        category = models.ProductCategory.objects.filter(
            product_type=type).get(product_category=category)
    except:
        category = models.ProductCategory.objects.create(
            product_type=type, product_category=category)

    return category