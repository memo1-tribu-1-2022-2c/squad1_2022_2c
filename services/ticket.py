from config import db

class TicketService():

    def __init__(self):
        self.cursor = db.cursor()

    def get_all_tickets(self):
        
        self.cursor.execute("SELECT * FROM tickets;")
        tickets = self.cursor.fetchall()
        values = [{'ticket_id': value[0], 'ticket_title': value[1]} for value in tickets]
        return values



