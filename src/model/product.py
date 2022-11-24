
SUPORTED = 'Con soporte'
DEPRECATED = 'Deprecada'


class Product():

    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
        self.versions = []

    def can_be_persisted(self) -> bool:

        return len(self.versions) >= 1

    def add_version(self, version):

        self.versions.append(version)

    def has_id(self, id: int) -> bool:
        return self.id == id

    def get_versions(self) -> list:

        return self.versions
        
    
class Version():

    def __init__(self, id: int, number: str, state: str, product: Product):
        self.id = id
        self.number = number
        self.state = state
        self.product = product.id
        self.persisted = False

        product.add_version(self)

    def associated_to(self, product: Product) -> bool:

        return product.has_id(self.product)

    def persist(self):
        """
            Persists the version if not persisted (changed or newly created)
        """
        if self.persisted:
            return