import mysimplehttp.api as http
from mysimplehttp import exception

import pytest

class TestScheme:

    def test_scheme_not_found(self):
        with pytest.raises(exception.SchemeNotFoundException):
            http.get('httpbin.org')

    def test_invalid_scheme(self):
        with pytest.raises(exception.InvalidSchemeException):
            http.get('htp://httpbin.org')
