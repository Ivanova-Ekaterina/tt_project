from flask import Flask
import sys
from app.config import ProductionConfig, TestingConfig
from authlib.flask.client import OAuth
from flask_jsonrpc import JSONRPC

from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.cache import SimpleCache
from flask_caching import Cache
from werkzeug.contrib.profiler import ProfilerMiddleware


app = Flask(__name__)
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

isonrpc = JSONRPC(app, '/api/')
oauth = OAuth(app)
app.config.from_object(TestingConfig)
cache = MemcachedCache(['127.0.0.1:11211'])

#from .views import *
from .handlers import *
