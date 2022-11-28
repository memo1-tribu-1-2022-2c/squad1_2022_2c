from flask_restful import Resource, reqparse
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from services.client import ClientService
from .product import ProductResponse

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

class ClientsNewProduct(Schema):

    client_id = fields.Str(default="NotFound", required=True);
    version_id = fields.Str(default="NotFound", required=True);

class ClientProductsSchema(Schema):
    client = fields.Nested(ClientResponse)
    products = fields.List(fields.Nested(ProductResponse))

class ClientNotFound(Schema):

    error = fields.Str(default="Client not found");

class ClientSearchResource(MethodResource, Resource):

    @doc(description="Returns a client based on its param", tags=["Clients"])
    @marshal_with(ClientResponse)
    @marshal_with(ClientNotFound, code='404')
    @use_kwargs(ClientQuery, location='query')
    def get(self, **kwargs):
        try:
            
            return client_service.get_by_param(kwargs['query']).to_json()
        except:
            
            return {
                'error': f'client: {kwargs["query"]} not found',
            }, '404'

    

class ClientWithVersionsResource(MethodResource, Resource):
    @doc(description="Associates a client with a version of a product", tags=["Clients"])
    @use_kwargs(ClientsNewProduct)
    @marshal_with(ClientsNewProduct)
    @marshal_with(ClientNotFound, code='404')
    def post(self, **kwargs):
        try:
            client_service.add_product(**kwargs)
            return kwargs
        except Exception as exception:
            return {
                'error': exception.args[0]
            }, '404'

    @doc(description="Returns all products from a client", tags=["Clients"])
    @use_kwargs(ClientQuery, location='query')
    @marshal_with(ClientProductsSchema)
    @marshal_with(ClientNotFound, code='404')
    def get(self, **kwargs):
        try:
            return client_service.get_all_products(kwargs['query'])
        except Exception as exception:
            return{
                'error': exception.args[0]
            }, '404'


class ClientDumpResource(MethodResource, Resource):

    @doc(description="Returns all clients in the system", tags=["Clients"])
    @marshal_with(ClientListSchema)
    @marshal_with(ClientNotFound, code='404')
    def get(self):
        try:

            clients = client_service.get_all()
        
            return {
                'clients': [client.to_json() for client in clients]
            }
        except:
            return {
                'error': 'Some unexpected error occured'
            }, '404'

    