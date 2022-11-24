from config import api, app, docs
from resources.ticket import TicketResource, TicketSearchResource, TicketSearchModify
from resources.client import ClientSearchResource, ClientDumpResource
from resources.product import ProductResource, ProductSearchResource
from resources.version import VersionResource, VersionSearchResource


# Add resources to API

'''
    Ticket resources
'''
api.add_resource(TicketResource, '/ticket')
api.add_resource(TicketSearchResource, '/ticket/<string:ticket_id>')
api.add_resource(TicketSearchModify, '/ticket/<string:ticket_id>')

'''
    Client resources
'''

api.add_resource(ClientSearchResource, '/client/search')
api.add_resource(ClientDumpResource, '/clients')


'''
    Product Resources
'''
api.add_resource(ProductSearchResource, '/product/<string:product_id>')
api.add_resource(ProductResource, '/product')

'''
    Version Resources
'''

api.add_resource(VersionSearchResource, '/version/<string:version_id>')
api.add_resource(VersionResource, '/version')

# Register Resources for swagger

'''
    Ticket docs
'''
docs.register(TicketResource)
docs.register(TicketSearchResource)
docs.register(TicketSearchModify)


'''
    Client docs
'''
docs.register(ClientSearchResource)
docs.register(ClientDumpResource)

'''
    Product docs
'''
docs.register(ProductResource)
docs.register(ProductSearchResource)

'''
    Version docs
'''
docs.register(VersionResource)
docs.register(VersionSearchResource)

if __name__ == "__main__":
    app.run(port=8000, debug=True)