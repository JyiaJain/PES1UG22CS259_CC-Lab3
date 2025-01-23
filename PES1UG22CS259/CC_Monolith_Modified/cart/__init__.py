import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    product_ids = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        evaluated_contents = json.loads(contents)
        product_ids.extend(evaluated_contents)

    products_map = products.get_products(product_ids) 
    cart_items = [products_map[product_id] for product_id in product_ids if product_id in products_map]
    
    return cart_items


    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


