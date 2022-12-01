from config import db, connect_and_return, try_commit, rollback

class TicktData():
    
    def __init__(self):
        self.table = 'tickets'
        self.cursor = db.cursor()

    def get_all(self) -> list:
        self.renew_cursor()
        try:
            self.cursor.execute(f"SELECT * FROM {self.table};")
        except:
            rollback()
            raise Exception("Could not get products")

        tickets = self.cursor.fetchall()
        try_commit()
        return tickets

    def get_by_client(self, client_id):
        self.renew_cursor()
        query = f"SELECT * FROM {self.table} WHERE client_id=%s"
        args = (client_id,)
        try:
            self.cursor.execute(query, args)
        except:
            rollback()
            raise Exception(f"Could not find tickets from {client_id}")
        tickets = self.cursor.fetchall();
        
        return tickets

    def get_by_id(self, ticket_id : int):
        self.renew_cursor()
        get_query = f"SELECT * FROM {self.table} WHERE id = %s"
        try:

            self.cursor.execute(get_query, (ticket_id,))
        except:
            rollback()
            raise Exception(f"Could not get ticket: {ticket_id}")
        ticket = self.cursor.fetchone()
        try_commit()
        return ticket

    def create(self, kwargs):
        self.renew_cursor()
        insert_query = f"INSERT INTO {self.table} (start_dt, title, client_id, project_id, version_id, description, state, person_in_charge, end_dt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        record_to_insert = (kwargs['ticket_start_dt'], kwargs['ticket_title'], kwargs['ticket_client_id'],\
        kwargs['ticket_project_id'], kwargs['ticket_version_id'], kwargs['ticket_description'], kwargs['ticket_state'],\
        kwargs['ticket_person_in_charge'], kwargs['ticket_end_dt'])
        try:
            self.cursor.execute(insert_query, record_to_insert)
        except:
            rollback()
            raise Exception("Could not create ticket")
        try_commit()
        self.cursor.execute(f"SELECT * FROM {self.table} ORDER BY id DESC LIMIT 1;")
        ticket = self.cursor.fetchone()
        return ticket
    
    def update(self, kwargs):
        update_query = """UPDATE tickets SET %s WHERE id = %s"""
        record_to_update = (kwargs['ticket_title'], kwargs['ticket'])
        self.renew_cursor()
        query, id = self.find_query(kwargs)
        try:
            self.cursor.execute(query, id)
        except:
            rollback()
            raise Exception("Could not update ticket")
        try_commit()
        return self.get_by_id(id)
        
    def find_query(kwargs):
        query = ""
        id = kwargs.pop('ticket_id')
        for i, label, value in kwargs.items:
            query += f"{label}={value}"
            if(i < len(kwargs.keys())):
                query += ", "
        return query,id

    def renew_cursor(self):
        if self.cursor.closed:
            data_base = connect_and_return()
            self.cursor = data_base.cursor()