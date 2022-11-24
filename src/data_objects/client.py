from typing import Type
import requests


CLIENTROUTE = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes"

class ClientData():
    """
        Class that returns querys to the client service
    """
    @staticmethod
    def get_all() -> list:
        values = requests.get(CLIENTROUTE).json()
        return values

    @staticmethod
    def _get_and_filter(filter_function: any):
        values = ClientData.get_all()
        return list(filter(filter_function, values))
        
    @staticmethod
    def get_by_id(id: int):
        return ClientData._get_and_filter(lambda client: client['id'] == id)

    @staticmethod
    def get_by_cuit(cuit: str):
        return ClientData._get_and_filter(lambda client: client['CUIT'] == cuit)

    @staticmethod
    def get_by_reason(social_reason: str):
        return ClientData._get_and_filter(lambda client: client['razon social'] == social_reason)