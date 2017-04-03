import logging.config
import os

from flask import Flask

import settings
from api.endpoints import api

Wapi = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


# loading namespaces to init


def initialize_app(flask_app):
	configure_app(flask_app)


def configure_app(flask_app):
	# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
	flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
	flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
	flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
	flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def main():
	env_flask_config_name = os.getenv('FLASK_ENV')
	if env_flask_config_name:
		log.warning('running on production')
		print 'running on production'
		# app.run(debug=False)
	else:
		initialize_app(Wapi)
		log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format('http://127.0.0.1:5000'))
		api.init_app(Wapi)
		Wapi.run(debug=settings.FLASK_DEBUG, use_reloader=False)


if __name__ == '__main__':
	main()
