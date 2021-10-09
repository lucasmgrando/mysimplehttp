import mysimplehttp.api as http
import io

class TestTest:

    def test_test(self):
        r1 = http.post('http://localhost:8000/login', {'pass': '123456789'})
        assert 'session' in r1.cookies

        f = io.StringIO('HOLA')
        r2 = http.post('http://localhost:8000/upload', files=dict(file=f), headers={
            'Cookie': 'session=' + r1.cookies['session']
        })

        assert r2.status == 302
