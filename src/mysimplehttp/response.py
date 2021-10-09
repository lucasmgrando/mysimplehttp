import json

class Response:
    def __init__(self, status, reason, headers, cookies, body):
        self.status = status
        self.reason = reason
        self.body = body
        self.headers = headers
        self.cookies = cookies

    @classmethod
    def create(self, response):
        """
            HTTPResponse to Response

            :param response: HTTPResponse
            :return: Response
        """
        headers_list = response.getheaders()
        headers = dict()
        for key, val in headers_list:
            headers[key] = val

        body = response.read()

        cookies = dict()
        if 'Set-Cookie' in headers:
            for kv in headers['Set-Cookie'].split(';'):
                k = kv.split('=')
                if len(k) > 1:
                    cookies[k[0]] = k[1]
                else:
                    cookies[k[0]] = ''

        return Response(response.status,
            reason=response.reason,
            headers=headers,
            cookies=cookies,
            body=body)

    def json(self):
        return json.loads(self.body)
