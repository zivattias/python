class BankAccountException(Exception):
    def __init__(self, s):
        super().__init__(s)

class MaxCreditReached(BankAccountException):
    def __init__(self):
        super().__init__('Maximum balance credit reached')
