# from reservations import Reservation
from datetime import datetime, timedelta

class Table:
    # Fixed table reservation duration:
    RESERVATION_DURATION = timedelta(hours=1, minutes=30)

    # INITIALIZE TABLE:
    def __init__(self, table_id: int, capacity: int):
        self.table_id = table_id
        self.capacity = capacity
        self.occupied_seats = 0
        self.is_available = True
        self.reservation_time: datetime | None = None
        self.reservation_limit: datetime | None = None
        # self.reservations: list[Reservation] = list()

    # VISUAL PRESENTATION OF 'TABLE':
    def __str__(self):
        return f"<TABLE #{self.table_id}>:\n" \
               f"- CAPACITY: {self.capacity}\n" \
               f"- OCCUPIED SEATS: {self.occupied_seats}\n" \
               f"- AVAILABLE? {self.is_available}\n" \
               f"- RESERVATION TIME: {self.reservation_time}\n" \
               f"- RESERVATION LIMIT: {self.reservation_limit}"

    # VISUAL NESTED REPRESENTATION of 'TABLE':
    def __repr__(self):
        return f"<TABLE #{self.table_id}, CAPACITY: {self.capacity}, " \
               f"TIME-LEFT: {datetime.now() - self.reservation_time}>"

    # Reserve a table as of now:
    def reserve(self, date: datetime.date, time: datetime.time):
        # reservation = Reservation(date, time)
        self.reservation_time = datetime.now()
        self.reservation_limit = self.reservation_time + self.RESERVATION_DURATION
        print(f"Table #{self.table_id} has been reserved on: {self.reservation_time}.")
        self.is_available = False

    # Get tables time limit:
    def get_tables_limit(self):
        return self.RESERVATION_DURATION

    # Update tables limit with a new value:
    def update_tables_limit(self, h: int, m: int):
        self.RESERVATION_DURATION = timedelta(hours=h, minutes=m)