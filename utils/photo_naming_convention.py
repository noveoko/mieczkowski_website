from utils.products import products
from .. import Config
categories = Config['PORTFOLIO_CATEGORIES']

data_set_sample = []

for product, examples in products.items():
    if categories.get(product, False): # Use get to avoid KeyError if product is not found
        print(product)
        for example in examples:
            example_desc = example['description']
            example_images = example['images']
            data_set_sample.append([product, example_desc, example_images[0]])
            if len(data_set_sample) >= 10: # Break loop once we have collected 10 items
                break
    else:
        print(f'Product {product} is turned off') # Inform the user and skip the product

    if len(data_set_sample) >= 10: # Need to break the outer loop as well
        break

#print(data_set_sample)
