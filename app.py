from flask import *

import init
from init import *
# from models import *

app = init.app

@app.route('/')
def index():
    log('index page', request.remote_addr)
    return render_template('main.html')


if __name__ == '__main__':
    port = conf['sys']['port']
    debug = conf['sys']['debug']
    app.run(host='0.0.0.0', port=port, debug=debug)
