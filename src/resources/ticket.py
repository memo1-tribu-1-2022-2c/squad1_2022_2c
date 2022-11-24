from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields, base
from src.config import psycopg2
from services.ticket import TicketService

ticket_service = TicketService()

class TicketResponse(Schema):
    ticket_id = fields.Int(default=-1)
    ticket_title = fields.Str(default='Not found')

class TicketCreate(Schema):
    ticket = fields.String(required=True)
    ticket_title = fields.Str(required=True)

class TicketUpdate(Schema):
    ticket = fields.String(required=True)
    ticket_title = fields.Str(required=True)

class MultipleTicketsResponse(Schema):
    tickets = fields.List(fields.Nested(TicketResponse))

class TicketSearchResource(MethodResource, Resource):

    @doc(description="Returns a ticket by its Id", tags=["Tickets"])
    @marshal_with(TicketResponse)
    def get(self, ticket_id):
        '''
            Ticket response
        '''
        ticket = ticket_service.get_ticket(ticket_id)
        return {'ticket': ticket}



class TicketResource(MethodResource, Resource):

    @doc(description="returns all tickets", tags=["Tickets"])
    @marshal_with(MultipleTicketsResponse)
    def get(self):
        '''
            Returns all tickets
        '''
        
        values = ticket_service.get_all_tickets()

        return {'tickets': values}

    @doc(description="Creates a new ticket", tags=['Tickets'])
    @use_kwargs(TicketCreate, location=('json'))
    @marshal_with(TicketResponse)
    def post(self, **kwargs):
        '''
            Creates a new ticket
        '''
        try:
            ticket_service.create_ticket(kwargs)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {
            'ticket': kwargs['ticket']
        }

        
class TicketSearchModify(MethodResource, Resource):
    @doc(description="Modify a ticket", tags=['Tickets'])
    @use_kwargs(TicketUpdate, location=('json'))
    @marshal_with(TicketResponse)
    def post(self, **kwargs):
        '''
            Update a ticket
        '''
        try:
            ticket_service.update_ticket(kwargs)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {
            'ticket': kwargs['ticket']
        }