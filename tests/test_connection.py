from mysimplehttp import exception, api as http, connection

class TestConnection:

    def test_pool_len(self):
        http.get('https://httpbin.org/get')
        http.get('https://google.com')
        http.get('https://httpbin.org/get')

        assert connection.pool_count == 2
