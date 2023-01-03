from threading import Thread, Lock
from exceptions import *


class BankAccount:

    def __init__(self, account_id: str):
        self._account_id = account_id
        self._balance = 0
        self._transactions: list = []
        self._lock = Lock()

    def balance(self):
        return self._balance

    def transactions(self):
        return self._transactions

    # @staticmethod
    # def lock_decorator(func):
    #     lock = Lock()
    #
    #     def decorated_func(*args, **kwargs):
    #         try:
    #             with lock:
    #                 func(*args, **kwargs)
    #         except BankAccountException as e:
    #             print(e)
    #         # finally:
    #         #     if lock.locked():
    #         #         lock.release()
    #
    #     return decorated_func

    # @lock_decorator
    def deposit(self, amount: int):
        with self._lock:
            self._balance += amount
            self._transactions.append('deposit')

    # @lock_decorator
    def withdraw(self, amount: int):
        if amount > self.balance():
            raise MaxCreditReached()
        with self._lock:
            self._balance -= amount
            self._transactions.append('withdraw')


if __name__ == '__main__':
    my_account = BankAccount("123456")


    def multiple_transactions_deposit(account):
        for i in range(100, 2_000_000, 10):
            account.deposit(i)


    def multiple_transactions_withdraw(account):
        for i in range(100, 2_000_000, 10):
            account.withdraw(i)


    t1 = Thread(target=multiple_transactions_deposit, args=(my_account,))
    t2 = Thread(target=multiple_transactions_deposit, args=(my_account,))
    t3 = Thread(target=multiple_transactions_withdraw, args=(my_account,))
    t4 = Thread(target=multiple_transactions_withdraw, args=(my_account,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    assert my_account._balance == 0, \
        f"Expected balance: 0, received: {my_account.balance()}"
    assert len(my_account._transactions) == 799960, \
        f"Expected transactions: 799960, received: {len(my_account.transactions())}"