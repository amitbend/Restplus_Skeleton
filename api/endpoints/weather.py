from flask_restplus import Resource, Namespace

ns = Namespace('weather', description="Add description")

import logging
logger = logging.getLogger(__name__)


@ns.route('')
class weather(Resource):
	def get(self):
		return {'result': 'dummy result'}, 200

