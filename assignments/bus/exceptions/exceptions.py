class LineExists(Exception):
    def __init__(self, line_num):
        self.msg = f'Line {line_num} already exists in db'
        super().__init__(self.msg)


class LineMissing(Exception):
    def __init__(self, line_num):
        self.msg = f'Line {line_num} is missing from db'
        super().__init__(self.msg)


class InvalidStopsString(Exception):
    def __init__(self):
        self.msg = 'Stops should be separated with a comma: a,b,c'
        super().__init__(self.msg)


class InvalidLineAttribute(Exception):
    def __init__(self, criteria):
        self.msg = f"Invalid line attribute (criteria): {criteria}"
        super().__init__(self.msg)
