import datetime


class BankAccount:

    def __init__(self, bank_name):
        self.name = bank_name

    @staticmethod
    def working_hours_only(open_hour: int = 9, close_hour: int = 17):
        def wrapper(func):
            def decorated(*args, **kwargs):
                now = datetime.datetime.now()
                day = now.weekday()
                time = now.time()
                opening_hour = datetime.time(open_hour, 0, 0)
                closing_hour = datetime.time(close_hour, 0, 0)

                if opening_hour < time < closing_hour and (0 <= day <= 3 or day == 6):
                    result = func(*args, **kwargs)
                    return result

                else:
                    raise Exception('Non-working hours')

            return decorated

        return wrapper

    @working_hours_only
    def withdraw(self, amount):
        print('Called withdraw', amount)
        return amount

    @working_hours_only
    def deposit(self, amount):
        print('Called deposit', amount)
        return amount

    @staticmethod
    def feedback(feedback_text):
        print('Called feedback')
        return feedback_text


if __name__ == '__main__':
    try:
        bank = BankAccount('hello-world')
        bank.deposit(500)
        bank.withdraw(500)
        bank.feedback('10/10')
    except Exception as e:
        print(e)
