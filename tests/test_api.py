import mysimplehttp.api as http
from mysimplehttp import exception

import logging
import io

logger = logging.getLogger(__name__)

class TestAPI:

    def test_get(self):
        r = http.get('http://httpbin.org/get')
        assert r.status == 200


    def test_post(self):
        r = http.post('http://httpbin.org/post')
        assert r.status == 200


    def test_post_with_files(self):
        f = io.StringIO('Hola')
        r = http.post('http://httpbin.org/post', dict(arg1='val1', arg2='val2'), files=dict(file=f))
        logger.debug(r.json())
        form = r.json()['form']
        assert form['arg1'] == 'val1'
        assert form['arg2'] == 'val2'
        assert 'file' in r.json()['files']


    def test_get_with_params(self):
        r = http.get('http://httpbin.org/get', dict(arg1='val1', arg2='val2'))
        args = r.json()['args']
        assert args['arg1'] == 'val1'
        assert args['arg2'] == 'val2'


    def test_post_with_params(self):
        r = http.post('http://httpbin.org/post', dict(arg1='val1', arg2='val2'))
        form = r.json()['form']
        assert form['arg1'] == 'val1'
        assert form['arg2'] == 'val2'


    def test_not_know_service(self):
        with pytest.raises(exceptions.MaxRetryError):
            http.get('http://notknowserviceorname.com')
