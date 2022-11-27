from config import db
from services.client import ClientService
from model.ticket import Ticket
import requests

class TicketService():

    def __init__(self):
        self.cursor = db.cursor()

    def get_all_tickets(self):
        tickets = Ticket.get_all()
        values = [{'ticket_id': value.get_id(), 'ticket_title': value.get_title()} for value in tickets]
        return values

    def get_ticket(self,ticket_id):
        ticket = Ticket.from_id(ticket_id)
        return {'ticket_id': ticket.get_id(), 'ticket_title': ticket.get_title()}


    def create_ticket(self, kwargs):
        client_service = ClientService()
        if(client_service.get_by_param(kwargs['ticket_client_id']) == None):
            return -1
        else:
            ticket = Ticket.create(kwargs)
            return ticket.get_id()

    def update_ticket(self, kwargs):
        ticket = Ticket.update(kwargs)
        return ticket.get_id()