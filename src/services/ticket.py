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
        if(client_service.get_by_param(kwargs['ticket_client']) == None):
            return -1
        else:
            ticket = Ticket.create(kwargs)
            return ticket.get_id()

    def find_query(kwargs):
        query = ""
        id = kwargs.pop('ticket_id')
        for i, label, value in kwargs.items:
            query += f"{label}={value}"
            if(i < len(kwargs.keys())):
                query += ", "
        return query,id

    def update_ticket(self, kwargs):
        update_query = """UPDATE tickets SET %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        self.cursor.execute(find_query(kwargs))
        db.commit()
        return self.cursor.rowcount