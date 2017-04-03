
from flask import Flask
from endpoints import api

app = Flask(__name__)
app.debug = False

api.init_app(app)
