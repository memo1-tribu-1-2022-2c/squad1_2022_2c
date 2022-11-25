from flask_restful import Resource, reqparse
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from services.client import ClientService


client_service = ClientService()

parser = reqparse.RequestParser()
parser.add_argument('by', type=str, location='args')


class ClientResponse(Schema):
    id = fields.Str(default="Client not found")
    razon_social = fields.Str(default="Client not found")
    CUIT = fields.Str(default="Client not found")

class ClientListSchema(Schema):

    clients = fields.List(fields.Nested(ClientResponse))

class ClientQuery(Schema):
    query = fields.Str(default="1")

class ClientSearchResource(MethodResource, Resource):

    @doc(description="Returns a client based on its param", tags=["Clients"])
    @marshal_with(ClientResponse)
    @use_kwargs(ClientQuery, location='query')
    def get(self, **kwargs):
        try:
            
            return client_service.get_by_param(kwargs['query']).to_json()
        except:
            
            return "Client not found", 404

class ClientDumpResource(MethodResource, Resource):

    @doc(description="Returns all clients in the system", tags=["Clients"])
    @marshal_with(ClientListSchema)
    def get(self):
        clients = client_service.get_all()
        
        return {
            'clients': [client.to_json() for client in clients]
        }