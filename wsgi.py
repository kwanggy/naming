if __name__ == '__main__':
    from app.config import conf, check_test_mode
    from app import app
    from werkzeug.contrib.fixers import ProxyFix

    if check_test_mode():
        port = conf['sys']['port']
    else:
        import os
        port = int(os.environ['PORT'])

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0', port=port)
