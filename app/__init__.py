from flask import Flask
from app.config import ProductionConfig
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
isonrpc = JSONRPC(app, '/api/')
app.config.from_object(ProductionConfig)

#from .views import *
from .handlers import *
