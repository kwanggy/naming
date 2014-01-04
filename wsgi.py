if __name__ == '__main__':
    from app.config import conf
    from app import app
    from werkzeug.contrib.fixers import ProxyFix

    port = conf['sys']['port']
    ops = { 'bind': '0.0.0.0:%s' % str(port) }

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0', port=port)
