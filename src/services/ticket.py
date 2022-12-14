from config import db
from services.client import ClientService
from model.ticket import Ticket
import requests

INVALID_TICKET = {"ticket_id":-1, "ticket_title":"Not Found"}

ERROR_INVALID_TICKET = 'Invalid ticket'
class TicketService():

    def __init__(self):
        self.cursor = db.cursor()

    def get_all_tickets_from(self, client_id):
        tickets = Ticket.get_all_by_client(client_id)
        return tickets

    def get_all_tickets(self):
        tickets = Ticket.get_all()
        
        return tickets

    def get_ticket(self,ticket_id):
        ticket = Ticket.from_id(ticket_id)
        return ticket.to_json()


    def create_ticket(self, kwargs):
        ticket = Ticket.create(kwargs)
        return ticket.to_json()



    def __validate_project(self, ticket_id, kwargs):
        try:
            actual_ticket = self.get_ticket(ticket_id)
            proyect = requests.get(f"https://squad2-2022-2c.herokuapp.com/api/v1/projects/{kwargs['ticket_project_id']}").json()
        
            if(proyect['clientId'] != actual_ticket['client_id']):
                raise ValueError("Error el nuevo proyecto no está asociado al mismo cliente")
        except ValueError:
            return  ERROR_INVALID_TICKET      

    def __validate_version(self, ticket_id, kwargs):
        try:
            actual_ticket = self.get_ticket(ticket_id)
            version = requests.get(f"https://squad2-2022-2c.herokuapp.com/api/v1/versions/{kwargs['ticket_version_id']}").json()
        
            if(version['projectId'] != actual_ticket['project_id']):
                raise ValueError("Error la versión no está asociada al mismo proyecto")
        except ValueError:
            return  ERROR_INVALID_TICKET      

    def __validate_args(self, ticket_id, kwargs):
        validation = self.__validate_project(ticket_id, kwargs)
        if(validation == ERROR_INVALID_TICKET):
            return INVALID_TICKET
        return self.__validate_version(ticket_id, kwargs)
            


    def update_ticket(self, ticket_id, kwargs):
        #validation = self.__validate_args(ticket_id, kwargs)
        #if(validation == ERROR_INVALID_TICKET):
        #    return INVALID_TICKET
        ticket = Ticket.update(ticket_id, kwargs)
        return ticket.to_json()
