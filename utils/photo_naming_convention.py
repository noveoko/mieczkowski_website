from utils.products import products
from .. import Config
categories = Config['PORTFOLIO_CATEGORIES']

product_database = []

for product, examples in products.items():
    if categories.get(product, False): # Use get to avoid KeyError if product is not found
        print(product)
        for example in examples:
            example_desc = example['description']
            example_images = example['images']
            product_database.append([product, example_desc, example_images])
            if len(product_database) >= 10: # Break loop once we have collected 10 items
                break
    else:
        print(f'Product {product} is turned off') # Inform the user and skip the product

