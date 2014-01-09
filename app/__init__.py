from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from util import log
from config import conf, load_default_conf


load_default_conf()
app = Flask(__name__)
app.config['SERVER_NAME'] = 'naming.cdo.li'
app.config['DEBUG'] = conf['sys']['debug']
app.config['SECRET_KEY'] = conf['sys']['secret_key']
db = conf['sys']['database']
if '://' not in conf['sys']['database']:
    import os
    db = os.environ[db]
app.config['SQLALCHEMY_DATABASE_URI'] = db
db = SQLAlchemy(app)


from flask_oauth import OAuth
from providers import get_provider
providers = dict()
for provider_id  in conf['sys']['providers']:
    module = get_provider(provider_id)
    con = dict(module.config)
    del con['id'], con['callback']
    for k, v in conf['sys'][provider_id].items():
        con[k] = v
    module.auth = OAuth().remote_app(**con)
    module.consumer_key = conf['sys'][provider_id]['consumer_key']
    module.consumer_secret = conf['sys'][provider_id]['consumer_secret']



from . import models, views
