import re
from model.client import Client


CLIENTROUTE = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes"

CUITREGEX = '^[0-9]{2}-[0-9]{8}-[0-9]{1}'

class ClientService():

    def __init__(self):
        self

    def get_all(self):
        return list(Client.get_all())

    def get_by_param(self, param: str):
        
        try:
            
            id = int(param)
            return Client.from_id(id)
        finally:
            
            if self.is_cuit(param):
                
                return Client.from_cuit(param)
            
            return Client.from_reason(param)


    def is_cuit(self, value: str) -> bool:
        matches = re.findall(CUITREGEX, value)
        if len(matches) != 1:
            return None

        return matches[0] == value