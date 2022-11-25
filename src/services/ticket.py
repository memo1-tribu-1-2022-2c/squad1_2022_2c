from config import db
from services.client import ClientService
from model.ticket import Ticket
import requests

class TicketService():

    def __init__(self):
        self.cursor = db.cursor()

    def get_all_tickets(self):
        
        self.cursor.execute("SELECT * FROM tickets;")
        tickets = self.cursor.fetchall()
        values = [{'ticket_id': value[0], 'ticket_title': value[2]} for value in tickets]
        return values

    def get_ticket(self,ticket_id):
        get_query = """SELECT * FROM tickets WHERE id = %s"""
        self.cursor.execute(get_query, (ticket_id,))
        ticket = self.cursor.fetchone()
        return {'ticket_id': ticket[0], 'ticket_title': ticket[2]}


    def create_ticket(self, kwargs):
        client_service = ClientService()
        if(client_service.get_by_param(kwargs['ticket_client']) == None):
            return -1
        else:
            ticket = Ticket.create(kwargs)
            return ticket.get_id()

    def update_ticket(self, kwargs):
        update_query = """UPDATE tickets SET title = %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        self.cursor.execute(update_query, record_to_update)
        db.commit()
        return self.cursor.rowcount