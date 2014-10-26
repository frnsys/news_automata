from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')

# Load config.
app.config.from_object('config')

# Setup the database.
db = MongoEngine(app)

# CORS so the concierge frontend can access the search endpoint.
CORS(app)

from . import routes
