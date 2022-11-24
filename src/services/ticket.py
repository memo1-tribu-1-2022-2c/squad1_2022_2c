from config import db
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
        clients = requests\
        .get("https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes")\
        .json()
        #No entiendo porque entra en el if si es siempre falso
        if({kwargs['ticket_client'] == value['razon social']} for value in clients):
            insert_query = """INSERT INTO tickets (start_dt, title, client, proyect_id, description, state, person_in_charge, end_dt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
            record_to_insert = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client'],\
                int(kwargs['ticket_proyect_id']), kwargs['ticket_description'], kwargs['ticket_state'],\
                kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
            self.cursor.execute(insert_query, record_to_insert)
            db.commit()
            self.cursor.execute("SELECT MAX(id) FROM tickets;")
            result = self.cursor.fetchone()
            return result[0]
        else:
            return -1

    def update_ticket(self, kwargs):
        update_query = """UPDATE tickets SET title = %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        self.cursor.execute(update_query, record_to_update)
        db.commit()
        return self.cursor.rowcount