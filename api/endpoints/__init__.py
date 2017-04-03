from weather import ns as ns1
from flask_restplus import Api

api = Api(
    title='Weather API',
    version='1.0',
    description='Check the endpoints to know more',
	prefix='/api'
    # All API metadatas
)

# add all namespaces here
api.add_namespace(ns1)
