from model.product import Product, Version, SUPORTED


class ProductService():

    
    def search_product(self, product_id: str):
        return Product.search_product(product_id).to_json()

    
    def new_product(self, **kwargs):
        name = kwargs['product']
        product = Product(name, 0)
        versions = [Version(0, value['number'], SUPORTED, product) for value in kwargs['versions']]
        product.store()
        

        return product.to_json()