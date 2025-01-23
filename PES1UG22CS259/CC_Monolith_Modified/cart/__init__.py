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
    # Fetch cart details from the DAO
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Collect all product IDs from the cart contents
    product_ids = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        # Use json.loads for safer parsing
        evaluated_contents = json.loads(contents)
        product_ids.extend(evaluated_contents)
    
    # Fetch all product details in a single batch request
    products_map = products.get_products(product_ids)  # Assume this returns a dictionary {id: Product}
    
    # Map product IDs to their corresponding Product objects
    cart_items = [products_map[product_id] for product_id in product_ids if product_id in products_map]
    
    return cart_items


    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


