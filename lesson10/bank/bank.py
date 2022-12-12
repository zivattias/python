import datetime


class Person:

    def __init__(self, person_id: str, name: str, address: str, phone: str):
        self.id = person_id
        self.name = name
        self.address = address
        self.phone = phone


class Transaction:

    def __init__(self, amount: float, currency: str, ts: datetime.datetime):
        self.amount = amount
        self.currency = currency
        self.ts = ts

    def __repr__(self):
        return f"{self.__class__.__name__} {self.amount} {self.currency}, {self.ts}"

    def __str__(self):
        return self.__repr__()


class Deposit(Transaction):
    pass

class Withdrawal(Transaction):
    pass

class Conversion(Transaction):
    def __init__(self, amount: float, currency: str, ts: datetime.datetime, rate: float):
        super().__init__(amount, currency, ts)
        self.rate = rate
    
    def __repr__(self):
        return f"{super().__repr__()}, rate: {self.rate}"


class BankAccount:

    def __init__(self, bank_name: str, branch: str, account_num: int, holders: set[Person],
                 usd_allowed: bool = False, credit_limit: float = 0):
        self.bank_name: str = bank_name
        self.branch: str = branch
        self.account_num: int = account_num
        self.holders: set[Person] = holders

        self.nis_balance: float = 0
        self.usd_balance: float = 0
        self.usd_allowed: bool = usd_allowed
        self.nis_credit_limit: float = credit_limit

        self.transactions: dict[datetime.date: list[Transaction]] = {}

    def __str__(self):
        return f"Account {self.account_num}"

    @staticmethod
    def _valid_params(amnt, currency):
        return amnt > 0 and currency in ('nis', 'usd')

    def _add_transaction(self, transaction: Transaction):
        transaction_date = datetime.date.today()

        # add new dictionary key if needed
        if transaction_date not in self.transactions:
            self.transactions[transaction_date] = []

        # if we are here, we are sure that the key already exists
        self.transactions[transaction_date].append(transaction)

    def withdraw(self, amount: float, currency: str = 'nis') -> bool:

        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            if self.nis_balance - amount >= (self.nis_credit_limit * -1):
                self.nis_balance -= amount
            else:
                return False
        else:
            if self.usd_allowed and self.usd_balance >= amount:
                self.usd_balance -= amount
            else:
                return False
        self._add_transaction(Withdrawal(amount, currency, datetime.datetime.now()))
        return True

    def deposit(self, amount: float, currency: str = 'nis'):
        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            self.nis_balance += amount
            self._add_transaction(Deposit(amount, currency, datetime.datetime.now()))
            return True
        else:
            if not self.usd_allowed:
                return False
            else:
                self._add_transaction(Deposit(amount, currency, datetime.datetime.now()))
                self.usd_balance += amount

    def convert_to_usd(self, nis_amnt, nis2usd_exchange_rate):
        if nis_amnt < 0:
            return False
        if not self.usd_allowed or self.nis_balance - nis_amnt < (self.nis_credit_limit * -1):
            return False
        self.nis_balance -= nis_amnt
        self.usd_balance += nis_amnt * nis2usd_exchange_rate
        self._add_transaction(Conversion(nis_amnt, "NIS", datetime.datetime.now(), nis2usd_exchange_rate))
        return True

    def convert_to_nis(self, usd_amnt, usd2nis_exchange_rate):
        if usd_amnt < 0:
            return False
        if not self.usd_allowed or self.usd_balance < usd_amnt:
            return False
        self.nis_balance += usd_amnt * usd2nis_exchange_rate
        self.usd_balance -= usd_amnt
        self._add_transaction(Conversion(usd_amnt, "USD", datetime.datetime.now(), usd2nis_exchange_rate))
        return True

    def get_current_balance(self) -> tuple[float, float]:
        return self.nis_balance, self.usd_balance

    def get_transactions_per_date(self, date: datetime.date) -> list[Transaction]:
        return self.transactions.get(date, [])


if __name__ == '__main__':
    # create bank account
    account1 = BankAccount('Discount', 'Kiryat Hasharon', 12345,
                           {Person('123456789', 'Valeria', 'Netanya', '054-444-4444')},
                           usd_allowed=True, credit_limit=10_000)
    print(f"Current balance for {account1}: {account1.get_current_balance()}")

    print("Trying to withdraw 10500 shekels passing the limit - should fail!")
    result = account1.withdraw(10500)
    print(f"Result: {result}")

    print("Trying to withdraw 9500 shekels in the range of limit - should succeed!")
    result = account1.withdraw(9500)
    print(f"Result: {result}")

    print(f"Current balance: {account1.get_current_balance()}")

    print("Trying to convert 1000 shekels to USD - outside the limit, should fail")
    result = account1.convert_to_usd(1000, 3.5)
    print(f"Result: {result}")

    print("Deposit 20_000 to account - should succeed")
    result = account1.deposit(20000)
    print(f"Result: {result}")

    print("Deposit $5_000 to account - should succeed")
    result = account1.deposit(5000, currency='usd')
    print(f"Result: {result}")

    print(f"New balance: {account1.get_current_balance()}")
    print(f"Transactions: {account1.get_transactions_per_date(datetime.date.today())}")
