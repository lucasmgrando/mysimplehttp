from .connection import get_connection
from .exception import MaxRetryError
from .response import Response

from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

def request(method, url, body=None, headers={}, retries=3, redirect=False):
    url = urlparse(url)
    conn = get_connection(url)

    conn.request(method, url.path + '?' + url.query, body=body, headers=headers)
    response = conn.getresponse()
    logger.debug(body)

    return Response.create(response)

"""
def request(method, url, body=None, headers=None, retries=3, redirect=False):
    conn = get_connection(url)

    while True:
        try:
            conn.request(method, '/', body=body, headers=headers)
            response = conn.getresponse()
        except socket.gaierror:
            retries = retries - 1
            if retries < 1
                raise MaxRetryError()

    if redirect and response.status in [301, 302]:
        response = request(method, response.headers['Location'], body, headers,
            retries, redirect)

    return response
"""
