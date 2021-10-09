from .request import request

from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)

def post(url, params={}, headers={}, files={}, retries=3):
    body = ''
    if params and not files:
        body = urlencode(params)
        headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

    if files:
        headers.update({'Content-Type': 'multipart/form-data;boundary="boundary"'})
        for k, v in params.items():
            body += '--boundary\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'.format(k, v)
        for k, v in files.items():
            body += '--boundary\r\nContent-Disposition: form-data; name="{}"; filename="archivo.txt"\r\n\r\n{}\r\n'.format(k, v.read())
        body += '--boundary--\r\n'
    logger.debug(body)

    return request('POST', url, body, headers, retries)


def get(url, params=None, headers={}, retries=3, redirect=False):
    if params:
        url += '?' + urlencode(params)

    return request('GET', url, headers=headers, retries=retries, redirect=redirect)
