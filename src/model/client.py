from typing import Type
from data_objects.client import ClientData
from .product import Version


IDKEY = 'id'
REASONKEYFROM = 'razon social'
REASONKEYTO = 'razon_social'
CUITKEY = 'CUIT'

class Client():

    def __init__(self, id: int, social_reason: str, cuit: str):
        self.id = id
        self.social_reason = social_reason
        self.cuit = cuit

    @staticmethod
    def from_json(json: dict):
        try:
            id = int(json[IDKEY])
            social_reason = json[REASONKEYFROM]
            cuit = json[CUITKEY]
            return Client(id, social_reason, cuit)
        except:
            return None

    def to_json(self) -> dict:
        json = {
            IDKEY: self.id,
            REASONKEYTO: self.social_reason,
            CUITKEY: self.cuit
        }

        return json

    @staticmethod
    def from_id(id: int):
        return Client.from_json(ClientData.get_by_id(id)[0])

    @staticmethod
    def from_cuit(cuit: str):
        return Client.from_json(ClientData.get_by_cuit(cuit)[0])

    @staticmethod
    def from_reason(reason: str):
        return Client.from_json(ClientData.get_by_reason(reason)[0])

    @staticmethod
    def get_all() -> list:
        values = ClientData.get_all();

        return list(map(lambda dict: Client.from_json(dict), values))

    
    def associate(self, version_id: int):
        ClientData.associate_client_and_product(self.id, version_id)

    def get_all_versions(self):
        '''
            Returns all versions that the client has associated
        '''
        try:
            version_ids = ClientData.get_all_products(self.id)
        except:
            raise Exception(f"Client: {self.id} was not found")

        try:
            productos = Version.retrieve_all_by_ids(version_ids)
        except:
            raise Exception("Some issue happened")

        return {
            'client': self.to_json(),
            'products': [producto.to_json() for producto in productos]
        }