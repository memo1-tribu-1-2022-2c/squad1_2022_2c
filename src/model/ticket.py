from data_objects.ticket import TicktData

ticket_db = TicktData()

class Ticket():

    def __init__(self, id: int, start_dt: str, title: str, client_id: str, proyect_id: int,\
    version_id: int, description: str, state: str, person_in_charge: str, end_dt: str):
        self.id = id
        self.start_dt = start_dt
        self.title = title
        self.client_id = client_id
        self.proyect_id = proyect_id
        self.version_id = version_id
        self.description = description
        self.state = state
        self.person_in_charge = person_in_charge
        self.end_dt = end_dt

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_all() -> list:
        tickets = ticket_db.get_all()
        all_tickets = []
        for ticket in tickets:
            all_tickets.append(Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[9]))
        return all_tickets
    
    @staticmethod
    def from_id(ticket_id: int):
        ticket = ticket_db.get_by_id(ticket_id)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[9])

    @staticmethod
    def create(kwargs):
        ticket = ticket_db.create(kwargs)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[9])

    def update(kwargs):
        ticket = ticket_db.update(kwargs)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[9])
    