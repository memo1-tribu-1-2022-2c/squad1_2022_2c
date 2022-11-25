from data_objects.ticket import TicktData

class Ticket():

    def __init__(self, id: int, start_dt: str, title: str, client: str, proyect_id: int,\
    description: str, state: str, person_in_charge: str, end_dt: str):
        self.id = id
        self.start_dt = start_dt
        self.title = title
        self.client = client
        self.proyect_id = proyect_id
        self.description = description
        self.state = state
        self.person_in_charge = person_in_charge
        self.end_dt = end_dt

    def get_id(self):
        return self.id
    
    @staticmethod
    def from_id(ticket_id: int):
        ticket = TicktData.get_by_id(ticket_id)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8])

    @staticmethod
    def create(**kwargs):
        ticket = TicktData.create(kwargs)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8])
