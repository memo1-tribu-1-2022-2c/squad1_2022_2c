from config import api, app, docs
from resources.ticket import TicketResource, TicketSearchResource


api.add_resource(TicketResource, '/ticket')
api.add_resource(TicketSearchResource, '/ticket/<string:ticket_id>')
docs.register(TicketResource)
docs.register(TicketSearchResource)

if __name__ == "__main__":
    app.run(port=8000, debug=True)