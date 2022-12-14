class LineExists(Exception):
    def __init__(self, line_num):
        super().__init__(f'Line {line_num} already exists in db')


class LineMissing(Exception):
    def __init__(self, line_num):
        super().__init__(f'Line {line_num} is missing from db')


class InvalidStopsString(Exception):
    def __init__(self):
        super().__init__('Stops should be separated with a comma: a,b,c')


class InvalidLineAttribute(Exception):
    def __init__(self, criteria):
        super().__init__(f"Invalid line attribute (criteria): {criteria}")
