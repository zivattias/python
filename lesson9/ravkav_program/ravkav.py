import datetime

class Card:

    SHORT_RIDE_LENGTH: list[int] = [0, 15]
    SHORT_RIDE_FEE: float = 5.5

    MEDIUM_RIDE_LENGTH: list[int] = [15, 40]
    MEDIUM_RIDE_FEE: int = 12

    LONG_RIDE_FEE: int = 23

    def __init__(self, holder_id: str, holder_name: str):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance: int = 0
        #   log: {SHORT_RIDE: 10,
        #         MEDIUM_RIDE: 5,
        #         LONG_RIDE: 3}
        self.__rides_log_by_type: dict[str, int] = dict()
        #   log: {4/12/2022: 4,
        #         5/12/2022: 3}
        self.__rides_log_by_date: dict[datetime.date: int] = dict()

    def get_holder_id(self) -> str:
        return self.__holder_id

    def set_holder_id(self, new_id: str):
        self.__holder_id = new_id

    def get_holder_nane(self) -> str:
        return self.__holder_name

    def set_holder_name(self, new_name: str):
        self.__holder_name = new_name

    def get_balance(self) -> int:
        return self.__balance

    def deduct_balance(self, amount: float):
        self.__balance -= amount

    def set_balance(self, amount: float):
        if amount <= 0:
            print("Invalid amount to load to card.")
            return False
        self.__balance += amount

    def log_ride_by_type(self, ride_type: str):
        if ride_type in self.__rides_log_by_type:
            self.__rides_log_by_type[ride_type] += 1
        self.__rides_log_by_type[ride_type] = 1

    def log_ride_by_date(self, date: datetime):
        if date in self.__rides_log_by_date:
            self.__rides_log_by_date[date] += 1
        self.__rides_log_by_date[date] = 1

    def get_rides_by_type(self):
        return self.__rides_log_by_type

    def get_rides_by_date(self):
        return self.__rides_log_by_date

    def ride(self, km: int, date: str):

        date_format = datetime.datetime.strptime(date, "%d-%m-%Y")
        if self.get_balance() < self.SHORT_RIDE_FEE:
            print("Insufficient funds for minimum ride fee.")
            return False
        if km == 0:
            print("Invalid KM amount to drive.")
            return False
        if date_format < datetime.date.today():
            print("Can't execute a ride for a retroactive datetime.")
            return False

        if self.SHORT_RIDE_LENGTH[0] < km <= self.SHORT_RIDE_LENGTH[1]:
            self.deduct_balance(self.SHORT_RIDE_FEE)
            ride_type = "SHORT"
        if self.MEDIUM_RIDE_LENGTH[0] < km <= self.MEDIUM_RIDE_LENGTH[1]:
            self.deduct_balance(self.MEDIUM_RIDE_FEE)
            ride_type = "MEDIUM"
        else:
            self.deduct_balance(self.LONG_RIDE_FEE)
            ride_type = "LONG"
        self.log_ride_by_type(ride_type)
        self.log_ride_by_date(date_format)
