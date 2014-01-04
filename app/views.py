from flask import *
from flask.ext.security import LoginForm, current_user, login_required, \
    login_user
from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler

from . import app, db
from .config import conf
from util import log


@app.route('/')
def index_page():
    log('index page', request.remote_addr)
    return render_template('index.html')

@app.route('/signin')
def signin_page():
    log('login page', request.remote_addr)
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    return redirect(request.referrer or '/')
    return render_template('login.html')

@app.route('/signup/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    provider = get_provider_or_404(provider_id)
    connection_values = session.get('failed_login_connection', None)

    ds = current_app.security.datastore
    user = ds.create_user(email=form.email.data, password=form.password.data)
    ds.commit()

    # See if there was an attempted social login prior to registering
    # and if so use the provider connect_handler to save a connection
    connection_values = session.pop('failed_login_connection', None)

    if connection_values:
        connection_values['user_id'] = user.id
        connect_handler(connection_values, provider)

    if login_user(user):
        ds.commit()
        flash('Account created successfully', 'info')
        return redirect(url_for('profile'))

    return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('register.html',
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)
