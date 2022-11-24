from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields

class ClientResponse(Schema):
    client = fields.Str(default="client not found")


class ClientCreateRequest(Schema):
    client = fields.String(required=True)

class ClientSearchResource(MethodResource, Resource):

    @doc(description="Returns a client based on its Id", tags=["Clients"])
    @marshal_with(ClientResponse)
    def get(self, client_id):
        '''
            Client GET
        '''
        return {
            'client': client_id
        }


class ClientResource(MethodResource, Resource):

    @doc(description="Creates a new client", tags=["Clients"])
    @use_kwargs(ClientCreateRequest)
    @marshal_with(ClientResponse)
    def post(self, **kwargs):

        return {
            'client': kwargs['client_id']
        }