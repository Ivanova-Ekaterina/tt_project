from flask import Flask
from app.config import ProductionConfig
from authlib.flask.client import OAuth
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
isonrpc = JSONRPC(app, '/api/')
oauth = OAuth(app)
app.config.from_object(ProductionConfig)

#from .views import *
from .handlers import *
