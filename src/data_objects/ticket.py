from config import db

class TicktData():
    
    def __init__(self):
        self.cursor = db.cursor()

    def get_all(self) -> list:
        self.cursor.execute("SELECT * FROM tickets;")
        tickets = self.cursor.fetchall()
        return tickets

    def get_by_id(self, ticket_id : int):
        get_query = """SELECT * FROM tickets WHERE id = %s"""
        self.cursor.execute(get_query, (ticket_id,))
        ticket = self.cursor.fetchone()
        return ticket

    def create(self, kwargs):
        insert_query = """INSERT INTO tickets (start_dt, title, client, proyect_id, description, state, person_in_charge, end_dt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        record_to_insert = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client'],\
        kwargs['ticket_proyect_id'], kwargs['ticket_description'], kwargs['ticket_state'],\
        kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
        self.cursor.execute(insert_query, record_to_insert)
        db.commit()
        self.cursor.execute("SELECT * FROM tickets ORDER BY id DESC LIMIT 1;")
        ticket = self.cursor.fetchone()
        return ticket
    
    def update(self, kwargs):
        update_query = """UPDATE tickets SET start_dt = %s, title = %s, client = %s, proyect_id = %s, description = %s\
            , state = %s, person_in_charge = %s, end_dt = %s,  WHERE id = %s"""
        record_to_update = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client'],\
        kwargs['ticket_proyect_id'], kwargs['ticket_description'], kwargs['ticket_state'],\
        kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
        self.cursor.execute(update_query, record_to_update)
        db.commit()