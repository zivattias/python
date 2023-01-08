class BadRequest(Exception):
    def __init__(self, request, status_code):
        super().__init__(f"Retrieved bad request: {request}, status code: {status_code}")