class WaterApp:

    def __init__(self):
        self.db = dict()
        self.total_cups_for_all = 0

    def signup(self, username: str):
        if username not in self.db:
            self.db[username] = {
                'total_cups': 0,
                'dates_dict': {

                }
            }

    def add_cup(self, username: str, date: str):
        """
        :param username:
        :param date:
        :return:
        """
        if username not in self.db:
            return None
        if date not in self.db[username]['dates_dict']:
            self.db[username]['dates_dict'][date] = 0
        self.db[username]['dates_dict'][date] += 1
        self.db[username]['total_cups'] += 1
        self.total_cups_for_all += 1

    def get_cups_per_user(self, username: str) -> int:
        return self.db[username]['total_cups']

    def get_cups_per_user_per_date(self, username: str, date: str) -> int:
        return self.db[username]['dates_dict'][date]