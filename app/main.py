from datetime import datetime
from wsgiref.util import request_uri


def application(env, start_resp):
    start_resp('200 OK', [('Content-Type', 'application/json')])
    url = request_uri(env)
    time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    test = '{"time":"' + time + '","url": "' + url + '"}'
    return [test.encode('utf-8')]
