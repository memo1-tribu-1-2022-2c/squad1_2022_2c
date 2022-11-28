from config import db

class TicktData():
    
    def __init__(self):
        self.table = 'tickets'
        self.cursor = db.cursor()

    def get_all(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table};")
        tickets = self.cursor.fetchall()
        return tickets

    def get_by_id(self, ticket_id : int):
        get_query = f"SELECT * FROM {self.table} WHERE id = %s"
        self.cursor.execute(get_query, (ticket_id,))
        ticket = self.cursor.fetchone()
        return ticket

    def create(self, kwargs):
        insert_query = f"INSERT INTO {self.table} (start_dt, title, client_id, project_id, version_id, description, state, person_in_charge, end_dt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        record_to_insert = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client_id'],\
        kwargs['ticket_project_id'], kwargs['ticket_version_id'], kwargs['ticket_description'], kwargs['ticket_state'],\
        kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
        self.cursor.execute(insert_query, record_to_insert)
        db.commit()
        self.cursor.execute(f"SELECT * FROM {self.table} ORDER BY id DESC LIMIT 1;")
        ticket = self.cursor.fetchone()
        return ticket
    
    def update(self, kwargs):
        update_query = """UPDATE tickets SET %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        query, id = self.find_query(kwargs)
        self.cursor.execute(query, id)
        db.commit()
        return self.get_by_id(id)
        
    def find_query(kwargs):
        query = ""
        id = kwargs.pop('ticket_id')
        for i, label, value in kwargs.items:
            query += f"{label}={value}"
            if(i < len(kwargs.keys())):
                query += ", "
        return query,id