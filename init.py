from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

from util import log
from config import *

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        load_conf(sys.argv[1])
else:
    if check_test_mode():
        load_conf('local.conf')
    else:
        load_conf('prod.conf')

app = Flask(__name__)
app.config['SECRET_KEY'] = conf['sys']['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = conf['sys']['database']
db = SQLAlchemy(app)

