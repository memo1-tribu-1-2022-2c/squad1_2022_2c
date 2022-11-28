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
        id = kwargs['ticket_project_id']
        proyect = requests.get(f"https://squad2-2022-2c.herokuapp.com/api/v1/projects/{id}").json()
        if(proyect['clientId'] != kwargs['ticket_client_id'] or proyect['versionId'] != kwargs['ticket_version_id']):
            return -1
        else:
            ticket = Ticket.create(kwargs)
            return ticket.get_id()


    def update_ticket(self, kwargs):
        ticket = Ticket.update(kwargs)
        return ticket.get_id()
