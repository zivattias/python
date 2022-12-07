from datetime import timedelta, datetime

class Reservation:

    RESERVATION_DURATION = timedelta(hours=1, minutes=30)

    def __init__(self, date: datetime.date, time: datetime.time):
        self.date = date
        self.time = time
        self.limit = self.time + self.RESERVATION_DURATION
