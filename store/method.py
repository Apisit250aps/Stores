def ShopCode(product_type:int, area:int, shop_id:int):
    
    return f"{int(product_type)*10}{int(area)*10}{1000+int(shop_id)}"