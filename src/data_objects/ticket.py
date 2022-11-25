from config import db

class TicktData():
    
    def __init__(self):
        self.cursor = db.cursor()

    def get_by_id(self, ticket_id : int):
        get_query = """SELECT * FROM tickets WHERE id = %s"""
        self.cursor.execute(get_query, (ticket_id,))
        ticket = self.cursor.fetchone()
        return ticket

    def create(self, **kwargs):
        insert_query = """INSERT INTO tickets (start_dt, title, client, proyect_id, description, state, person_in_charge, end_dt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        record_to_insert = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client'],\
        int(kwargs['ticket_proyect_id']), kwargs['ticket_description'], kwargs['ticket_state'],\
        kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
        self.cursor.execute(insert_query, record_to_insert)
        db.commit()
        self.cursor.execute("SELECT MAX(id) FROM tickets;")
        ticket = self.cursor.fetchone()
        return ticket