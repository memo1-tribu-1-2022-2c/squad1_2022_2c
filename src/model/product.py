from data_objects.product import ProductData
from data_objects.version import VersionData

SUPORTED = 'Con soporte'
DEPRECATED = 'Deprecada'

products_db = ProductData()
versions_db = VersionData()

class Product():

    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
        self.versions = []

    def to_json(self) -> dict:
        return {
            'product': self.name,
            'product_id': self.id,
            'versions': [version.to_json() for version in self.versions]
        }

    def change_id(self, new_id: int):
        self.versions = [version.set_product_id(new_id) for version in self.versions]
        self.id = new_id

    def can_be_persisted(self) -> bool:

        return len(self.versions) >= 1

    def add_version(self, version):

        self.versions.append(version)

    def has_id(self, id: int) -> bool:
        return self.id == id

    def get_versions(self) -> list:

        return self.versions

    @staticmethod
    def search_product(product_id: str):
        result = products_db.get_product_by_id(product_id)
        if not result:
            return None
        
        versions = versions_db.retrieve_version_by_product(int(product_id))
        product = Product(result['name'], result['id'])
        
        [Version(value[0], value[1], value[2], product) for value in versions]
        return product

    @staticmethod
    def search_products(product_ids: list):
        return [Product.search_product(product_id) for product_id in product_ids]

    def store(self):
        products_db.store_new_product(self)
        
        [version.persist() for version in self.versions]
    
    def update(self):
        products_db.update_product(self)

class Version():

    def __init__(self, id: int, number: str, state: str, product: Product):
        self.id = id
        self.number = number
        self.state = state
        self.product = product.id

        product.add_version(self)

    
    def set_product_id(self, new_id: int):
        self.product = new_id
        return self

    def change_state(self):

        self.state = SUPORTED if self.state == DEPRECATED else DEPRECATED

    def to_json(self) -> dict:

        return {
            'version_id': self.id,
            'number': self.number,
            'state': self.state
        }

    def update(self):
        versions_db.update_version(self)

    def associated_to(self, product: Product) -> bool:

        return product.has_id(self.product)

    def persist(self):
        """
            Persists the version if not persisted (changed or newly created)
        """
        versions_db.store_new_version(self)

    @staticmethod
    def retrieve_by_product(product_id: int):
        data = versions_db.retrieve_version_by_product(product_id)
        product = Product.search_product(product_id)
        
        return [Version(value[0], value[1], value[2], product) for value in data]

    @staticmethod
    def retrieve_by_id(version_id: int):
        data = versions_db.retrieve_version_by_id(version_id)
        
        product = Product.search_product(data[3])
        
        version = Version(data[0], data[1], data[2], product)

        return version

    @staticmethod
    def retrieve_all_by_ids(version_ids: list):
        versions = versions_db.retrieve_all_by_id(version_ids)
        product_ids = set([version[3] for version in versions])
        productos = Product.search_products(product_ids)
        
        mapa_versiones = {}

        for product_id in product_ids:
            product_versions = []
            for version in versions:
                if version[3] == product_id:
                    product_versions.append(version[0])
            mapa_versiones[product_id] = product_versions
        
        for product in productos:
            todas_versiones = product.get_versions()
            versiones_cliente = mapa_versiones[product.id]
            
            product.versions = list(filter(lambda version: version.id in versiones_cliente, todas_versiones))
            
        
        return productos
