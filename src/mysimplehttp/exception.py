class SchemeNotFoundException(Exception):
    def __init__(self):
        super().__init__('Scheme not found')

class InvalidSchemeException(Exception):
    def __init__(self, scheme):
        super().__init__(f'Invalid scheme: {scheme}')

class DNSResolutionError(Exception):
    pass

class MaxRetryError(Exception):
    pass
