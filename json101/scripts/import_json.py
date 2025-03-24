
#In this excercise, we would extract certain datas from a json file 
import json 

with open(r'api-scrapping\jsonfiles\2.json', 'r') as f:
    data = json.load(f)

product_id = [products['product_id'] for products in data['products']]
product_name = [products['name'] for products in data['products']]
product_price = [products['price'] for products in data['products']]
product_in_stock = [products['in_stock'] for products in data['products']]


products_data = {'product_id':product_id, 'product_name':product_name, 'product_price':product_price, 'product_in_stock':product_in_stock}

print(products_data)