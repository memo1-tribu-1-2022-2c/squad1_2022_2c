from model.product import Version, Product, SUPORTED


class VersionService():


    def store_new_version(self, **kwargs):

        product = Product.search_product(kwargs['product_id'])

        version = Version(0, kwargs['number'], SUPORTED, product)

        version.persist()

        return version.to_json()

    def get_by_product_id(self, product_id):

        versions = Version.retrieve_by_product(product_id)
        print([version.to_json() for version in versions])
        return [version.to_json() for version in versions]