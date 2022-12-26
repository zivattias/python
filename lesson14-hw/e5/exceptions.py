class AAPLException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidDirectory(AAPLException):
    def __init__(self, directory):
        super().__init__(f'Invalid directory given: {directory}')


class InvalidFile(AAPLException):
    def __init__(self, file):
        super().__init__(f'Invalid file given: {file}')
