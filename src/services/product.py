from model.product import Product, Version, SUPORTED


class ProductService():

    
    def search_product(self, product_id: str):

        product = Product.search_product(product_id)

        if not product: 
            raise Exception("Product not found")

        return product.to_json()

    def get_products(self):
        return {'products': Product.get_products()}
    
    def new_product(self, **kwargs):
        name = kwargs['product']
        product = Product(name, 0)
        versions = [Version(0, value['number'], SUPORTED, product) for value in kwargs['versions']]
        product.store()
        

        return product.to_json()

    def update_product(self, product_id: str, name=None):
        
        try: 
            product = Product.search_product(product_id)
        except:
            raise Exception("Product not found")

        if name:
            product.name = name

        try:
            product.update()
        except:
            raise Exception("Could not update product")

        return product.to_json()
