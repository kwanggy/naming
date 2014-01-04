from datetime import datetime
from dateutil import tz

tz_utc = tz.tzutc()
tz_local = tz.tzutc()

def set_timezone(timezone):
    tz_local = tz.gettz(timezone)

def now_str(form):
    d = datetime.utcnow()
    d = d.replace(tzinfo=tz_utc)
    d = d.astimezone(tz_local)
    now = d.strftime(form)
    return now

def log(*args):
    try:
        msg = u' '.join([unicode(x) for x in args])
        msg = msg.encode('utf-8')
    except Exception as e:
        print e
        msg =  'invalid msg'
    print now_str('%Y-%m-%d %H:%M:%S'), msg
