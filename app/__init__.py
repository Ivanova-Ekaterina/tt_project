from flask import Flask
from flask_cors import CORS
import sys
from flask_sqlalchemy import SQLAlchemy
from app.config import ProductionConfig, TestingConfig
#from authlib.flask.client import OAuth
from flask_jsonrpc import JSONRPC
from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.cache import SimpleCache
from flask_caching import Cache
from werkzeug.contrib.profiler import ProfilerMiddleware
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
cors = CORS(app)
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

isonrpc = JSONRPC(app, '/api/')
app.config.from_object(ProductionConfig)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ekaterina:@localhost/track_orm'
#oauth = OAuth(app)
#app.config.from_object(TestingConfig)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://quack:ewTe6pEFyIK@89.208.84.222/quack'
db = SQLAlchemy(app)
migrate = Migrate(db)

#cache = MemcachedCache(['127.0.0.1:11211'])

from .views import *
#from .handlers_old import *
from app import model
#from .task import *
