from util import set_timezone, log

conf = {
    'sys': {
        'debug': True,
        'port': 9020,
        'secret_key': None,
        'twitter_consumer_key': None,
        'twitter_consumer_secret': None,
        'facebook_consumer_key': None,
        'facebook_consumer_secret': None,
        'timezone': 'America/New_York',
        'verbose': True,
        'timeout': 120,
        'max_tries': 3,
        'test-mode': False,
    },
}

def load_conf(filename):
    import json
    __conf__ = None
    with open('conf/'+filename) as f:
        r = f.read()
        __conf__ = json.loads(r)

    if __conf__ == None:
        raise Exception('load configuration %s failed' % filename)

    for key in __conf__:
        c = conf[key]
        _c = __conf__[key]
        for subkey in _c:
            c[subkey] = _c[subkey]

    required = {
        'sys': [
            'twitter_consumer_key', 'twitter_consumer_secret',
            'facebook_consumer_key', 'facebook_consumer_secret'
        ]
    }
    for req in required:
        c = conf[req]
        for r in required[req]:
            if c[r] == None:
                raise ValueError('conf.%s.%s is None' % (req, r))

    check_test_mode()
    set_timezone(conf['sys']['timezone'])

def check_test_mode():
    try:
        with open('TEST') as f:
            pass
        log('TEST MODE')
        conf['test-mode'] = True
        return conf['test-mode']
    except:
        pass
    return False


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        load_conf(sys.argv[1])
        log(conf)
