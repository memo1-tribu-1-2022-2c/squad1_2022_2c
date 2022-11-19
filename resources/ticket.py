from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields

class TicketResponse(Schema):
    ticket = fields.Str(default="Not found")

class TicketCreate(Schema):
    ticket = fields.String(required=True)


class TicketSearchResource(MethodResource, Resource):

    @doc(description="Returns a ticket by its Id", tags=["Tickets"])
    @marshal_with(TicketResponse)
    def get(self, ticket_id):
        '''
            Ticket response
        '''
        return {'ticket': ticket_id}



class TicketResource(MethodResource, Resource):

    @doc(description="returns all tickets", tags=["Tickets"])
    @marshal_with(TicketResponse)
    def get(self):
        '''
            Returns all tickets
        '''
        return {'ticket': 'alltickets'}

    @doc(description="Creates a new ticket", tags=['Tickets'])
    @use_kwargs(TicketCreate, location=('json'))
    @marshal_with(TicketResponse)
    def post(self, **kwargs):
        '''
            Creates a new ticket
        '''
        return {
            'ticket': kwargs['ticket']
        }