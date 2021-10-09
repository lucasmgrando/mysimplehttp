from .exception import SchemeNotFoundException, InvalidSchemeException

from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import urlencode

pool = dict()

pool_count = 0

def get_connection(url):
    global pool_count

    conn = pool.get(url.netloc, None)
    if not conn:
        pool_count += 1
        conn = create_connection(url)

    return conn


def create_connection(url):
    scheme = url.scheme
    if scheme is None or scheme == '':
        raise SchemeNotFoundException()

    if not scheme in ['http', 'https']:
        raise InvalidSchemeException(scheme)

    if scheme == 'https':
        conn = HTTPSConnection(url.netloc)
    else:
        conn = HTTPConnection(url.netloc)

    pool[url.netloc] = conn

    return conn
