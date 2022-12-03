from data_objects.ticket import TicktData

ticket_db = TicktData()

class Ticket():

    def __init__(self, id: int, start_dt: str, title: str, client_id: str, project_id: int,\

    version_id: int, description: str, state: str, person_in_charge: str, end_dt: str, criticity: str):

        self.id = id
        self.start_dt = start_dt
        self.title = title
        self.client_id = client_id
        self.project_id = project_id
        self.version_id = version_id
        self.description = description
        self.state = state
        self.person_in_charge = person_in_charge
        self.end_dt = end_dt
        self.end_detail = ''
        self.criticity = criticity

    def to_json(self):
        return {
            'id': self.id,
            'start_dt': self.start_dt,
            'title': self.title,
            'client_id': self.client_id,
            'project_id': self.project_id,
            'version_id': self.version_id,
            'description': self.description,
            'state': self.state,
            'criticity': self.criticity,
            'person_in_charge': self.person_in_charge,
            'end_detail': self.end_detail,
            'end_dt': self.end_dt
        }

    def get_id(self):
        return self.id
#comentario
    @staticmethod
    def get_all_by_client(client_id):
        tickets = ticket_db.get_by_client(client_id)
        tickets_without_detail = [
            Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[10], ticket[11])
            for ticket in tickets
        ]
        for index, ticket in enumerate(tickets_without_detail):
            if ticket.state == "CERRADO":
                ticket.end_detail = tickets[index][9]
        jsons = [ticket.to_json() for ticket in tickets_without_detail]
        
        return jsons

    def get_title(self):
        return self.title

    def get_all() -> list:
        tickets = ticket_db.get_all()
        all_tickets = []
        for ticket in tickets:
            all_tickets.append(Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[10], ticket[11]))
        for index, ticket in enumerate(all_tickets):
            if ticket.state == "CERRADO":
                ticket.end_detail = tickets[index][9]
        
        return [ticket.to_json() for ticket in all_tickets]
    
    @staticmethod
    def from_id(ticket_id: int):
        ticket = ticket_db.get_by_id(ticket_id)
        pre_ticket = Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[10], ticket[11])
        if pre_ticket.state == "CERRADO":
            pre_ticket.end_detail = ticket[9]
        return pre_ticket

    @staticmethod
    def create(kwargs):
        ticket = ticket_db.create(kwargs)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[10], ticket[11])

    def update(kwargs):
        ticket = ticket_db.update(kwargs)
        return Ticket(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6], ticket[7], ticket[8], ticket[10], ticket[11])
    