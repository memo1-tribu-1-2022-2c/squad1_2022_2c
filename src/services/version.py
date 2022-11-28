from model.product import Version, Product, SUPORTED, DEPRECATED


class VersionService():

    def __init__(self):
        self.version_number = 'number'
        self.version_state = 'state'


    def store_new_version(self, **kwargs):

        product = Product.search_product(kwargs['product_id'])

        version = Version(0, kwargs['number'], SUPORTED, product)

        version.persist()

        return version.to_json()

    def get_by_product_id(self, product_id):

        versions = Version.retrieve_by_product(product_id)
        print([version.to_json() for version in versions])
        return [version.to_json() for version in versions]

    def modify_version(self, version_id=None, number=None, state_change=None):
        
            if not version_id:
                raise Exception("No version id given")

            version = Version.retrieve_by_id(version_id)

            if number:
                version.number = number

            if state_change:
                version.change_state()

            try:
                version.update()
            except:
                raise Exception("Some issue occured...")

            return version.to_json()

