from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social, SQLAlchemyConnectionDatastore, \
     login_failed
from flask.ext.social.utils import get_connection_values_from_oauth_response

from util import log
from config import conf, load_default_conf


load_default_conf()
app = Flask(__name__)
app.config['DEBUG'] = conf['sys']['debug']
app.config['SECRET_KEY'] = conf['sys']['secret_key']
db = conf['sys']['database']
if '://' not in conf['sys']['database']:
    import os
    db = os.environ[db]
app.config['SQLALCHEMY_DATABASE_URI'] = db
db = SQLAlchemy(app)


from . import models, views
