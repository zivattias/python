class TableException(Exception):
    pass


class TableNotFound(TableException):
    def __init__(self, table_id: int):
        super().__init__(f"Table {table_id} doesn't exist.")


class TableAlreadyOccupied(TableException):
    def __init__(self, table_id: int):
        super().__init__(f'Table {table_id} is already occupied.')


class InsufficientSeatsInTable(TableException):
    def __init__(self, table_id: int, table_seats: int, guests_num: int):
        super().__init__(f"Table {table_id} has only {table_seats} seats, can't accommodate {guests_num}.")


class TableAlreadyAvailable(TableException):
    def __init__(self, table_id: int):
        super().__init__(f"Table {table_id} is already available.")
