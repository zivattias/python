import bank
from datetime import datetime
now = datetime.now()
date_string = now.strftime("%d/%m/%Y")
date_string_split = date_string.split("/")
month = date_string_split[1]
year = date_string_split[2]

class Account:

    available_log_types = ['deposit', 'withdrawal', 'transfer_to', 'transfer_in', 'conversion']

    def __init__(self, account_id: int, credit_limit: int, is_foreign_currency: bool):
        self.account_id = account_id
        self.credit_limit = credit_limit
        self.is_foreign_currency = is_foreign_currency
        self.transaction_db = {}
        # '28/11/2022': {
        #       'deposit': 1000,
        #       'withdrawal': 100,
        #       'transfer_to': [account_id, 150, ILS]
        #       'transfer_in': [account_id, 200, USD],
        #       'conversion': {
        #           'from': [200, ILS],
        #           'to':   [58.25, USD],
        #           'fee':  [4.5, ILS]
        #       }
        #    }
        # }
        self.balance = [0, 0]

    def __str__(self):
        details = f'- ACCOUNT #{self.account_id} -\nCREDIT LIMIT: {self.credit_limit:,} ILS\n' \
                  f'BALANCES:\n{self.balance[0]:,} ILS'
        return details if not self.is_foreign_currency else details + '\n' + f"{self.balance[1]:,} USD"

    def __repr__(self):
        return f"<ACCOUNT: {self.account_id}>"

    # Log function to create db of performed actions in account
    # def log_transaction(self, tr_type: str, value: int):
    #     if tr_type not in self.available_log_types:
    #         error = f"ERROR: Failed to log unknown transaction type ({type})."
    #         print(error)
    #     if date_string not in self.transaction_db.keys():
    #         self.transaction_db[date_string] = {}
    #     if tr_type not in self.transaction_db[date_string].keys():
    #         self.transaction_db[date_string][tr_type] = value






