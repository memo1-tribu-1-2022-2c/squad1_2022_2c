from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields, base
from config import psycopg2
from services.ticket import TicketService

from flask_cors import cross_origin

ticket_service = TicketService()

class TicketCreate(Schema):
    ticket_start_dt = fields.Date(required=True)
    ticket_title = fields.Str(required=True)
    ticket_client_id = fields.Int(required=True)
    ticket_project_id = fields.Int(required=True)
    ticket_version_id = fields.Int(required=True)
    ticket_description = fields.Str(required=False)
    ticket_state = fields.Str(required=True)
    ticket_person_in_charge = fields.Str(required=True)
    ticket_end_dt = fields.Date(required=True)
    ticket_criticity = fields.Str(required=True)

class TicketUpdate(Schema):
    start_dt = fields.Date(required=False)
    title = fields.Str(required=False)

    client_id = fields.Int(required=False)
    project_id = fields.Int(required=False)
    version_id = fields.Int(required=False)
    description = fields.Str(required=False)
    state = fields.Str(required=False)
    person_in_charge = fields.Str(required=False)
    end_detail = fields.Str(required=False)
    end_dt = fields.Date(required=False)
    criticity = fields.Str(required=False)


class TicketQuery(Schema):
    id = fields.Str()
    start_dt = fields.Date()
    title = fields.Str()
    client_id = fields.Str()
    project_id = fields.Str()
    version_id = fields.Str()
    description = fields.Str()
    criticity = fields.Str()
    state = fields.Str()
    person_in_charge = fields.Str()
    end_detail = fields.Str()
    end_dt = fields.Str()

class MultipleTicketsQuery(Schema):
    tickets = fields.List(fields.Nested(TicketQuery))

class ClientNotFoundSchema(Schema):
    error = fields.Str()

class TicketSearchResource(MethodResource, Resource):

    @doc(description="Returns a ticket by its Id", tags=["Tickets"])
    @marshal_with(TicketQuery)
    def get(self, ticket_id):
        '''
            Ticket response
        '''
        ticket = ticket_service.get_ticket(ticket_id)
        return ticket



class TicketResource(MethodResource, Resource):

    @doc(description="returns all tickets", tags=["Tickets"])
    @marshal_with(MultipleTicketsQuery)
    def get(self):
        '''
            Returns all tickets
        '''
        
        values = ticket_service.get_all_tickets()

        return {'tickets': values}

    @doc(description="Creates a new ticket", tags=['Tickets'])
    @use_kwargs(TicketCreate, location=('json'))
    @marshal_with(TicketQuery)
    @cross_origin()
    def post(self, **kwargs):
        '''
            Creates a new ticket
        '''
        try:
            ticket = ticket_service.create_ticket(kwargs)
            return ticket
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise "Ticket could not be created"


class TicketSearchModify(MethodResource, Resource):
    @doc(description="Modify a ticket", tags=['Tickets'])
    @use_kwargs(TicketUpdate, location=('json'))
    @marshal_with(TicketQuery)
    @cross_origin()
    def patch(self, ticket_id, **kwargs):
        '''
            Update a ticket
        '''
        try:
            ticket = ticket_service.update_ticket(ticket_id, kwargs)
            return ticket
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {
                'ticket': ticket_id
            }, '404'

class TicketByClient(MethodResource, Resource):

    @doc(description="Returns all tickets by client id", tags=["Tickets"])
    @marshal_with(MultipleTicketsQuery)
    @marshal_with(ClientNotFoundSchema, code='404')
    def get(self, client_id):
        try:
            return {'tickets': ticket_service.get_all_tickets_from(client_id)}
        except:
            return {
                'error': f"Client {client_id} no fue encontrado"
            }
