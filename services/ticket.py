from config import db

class TicketService():

    def __init__(self):
        self.cursor = db.cursor()

    def get_all_tickets(self):
        
        self.cursor.execute("SELECT * FROM tickets;")
        tickets = self.cursor.fetchall()
        values = [{'ticket_id': value[0], 'ticket_title': value[1]} for value in tickets]
        return values

    def create_ticket(self, kwargs):
        insert_query = """INSERT INTO tickets (id, title) VALUES (%s, %s);"""
        record_to_insert = (kwargs['ticket'], kwargs['ticket_title'])
        self.cursor.execute(insert_query, record_to_insert)
        db.commit()
        return self.cursor.rowcount

    def update_ticket(self, kwargs):
        update_query = """UPDATE tickets SET title = %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        self.cursor.execute(update_query, record_to_update)
        db.commit()
        return self.cursor.rowcount
#hay que usar un cursor.close() y un connection.close()?