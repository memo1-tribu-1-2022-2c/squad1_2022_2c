from model.product import Product



class ProductService():

    
    def search_product(self, product_id: str):
        return Product.search_product(product_id)

    
    def new_product(self, **kwargs):
        name = kwargs['product']
        product = Product(name, 0)

        product.store()
        

        return product.to_json()