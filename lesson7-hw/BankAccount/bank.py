from bank_accounts import *
from bank_customers import *

class Bank:
    # CLASS VARIABLES:
    total_users = 0
    total_accounts = 0
    available_currencies = ["ILS", "USD"]
    usd_rate = 3.43

    # INITIALIZE BANK:
    def __init__(self, bank_name: str, bank_branch: str):
        self.bank_name: str = bank_name
        self.bank_branch_number: str = bank_branch
        self.bank_accounts = {int(): {'owners': list(),
                                      'account_details': Account}}
        # bank_accounts = {account_id: {owners: [customer_id, customer_id],
        #                               account_details: Account()}}
        self.bank_customers = {int(): Person}
        # bank_customers = {customer_id: Customer()}

    # ADD USER TO BANK:
    def add_user(self, customer_id: int, name: str, address: str, phone: str, email: str):

        user: Person = Person(customer_id, name, address, phone, email)

        # Check if user doesn't exist and create one:
        if customer_id not in self.bank_customers.keys():
            self.bank_customers[customer_id] = user
        # Update users counter:
            self.total_users += 1
            print(f"SUCCESS: User '{name}' has been added to the database as ID: {customer_id}.")
        # If a user exists, display an error and conclude the function:
        else:
            error = f'ERROR: A user with the same customer ID ({customer_id}) already exists in the system.'
            return print(error)

    # CREATE ACCOUNT TO USER / ADD USER TO EXISTING ACCOUNT:
    def create_account(self, customer_id: int, account_id: int, credit_limit: int,
                       is_foreign_currency: bool):

        account: Account = Account(account_id, credit_limit, is_foreign_currency)
        customer_id: int = customer_id
        account_id: int = account_id
        # Check if user doesn't exist in db:
        if customer_id not in self.bank_customers.keys():
            error = f"ERROR: Can't create account to a user that doesn't exist ({customer_id}). Add them first."
            return print(error)
        # Check if account doesn't exist and create one:
        else:
            if account_id not in self.bank_accounts.keys():
                self.bank_accounts[account_id] = {'owners': [], 'account_details': account}
            if customer_id not in self.bank_accounts[account_id]['owners']:
                self.bank_accounts[account_id]['owners'].append(customer_id)
            # Update accounts counter:
                self.total_accounts += 1
                print(f"SUCCESS: Account {account_id} has been created and assigned to {customer_id}.")
            # If account exists, add another owner to already created account:
            else:
                self.bank_accounts[account_id]['owners'].append(customer_id)

    # SHOW ACCOUNT'S OWNER(s):
    def display_account_owners(self, account_id: int):
        # Checks if account in db and displays relevant owners:
        if account_id in self.bank_accounts.keys():
            owners = self.bank_accounts[account_id]['owners']
            print(f'Account ID: {account_id}, belongs to: {owners}')
        # Presents an error if account doesn't exist:
        else:
            error = f"ERROR: No such account ID ({account_id}) in the system."
            return print(error)

    # SHOW CUSTOMER'S ACCOUNT(s):
    def display_owner_accounts(self, customer_id):
        accounts_list = list()
        # Checks if customer ID in db and display relevant accounts:
        for account in self.bank_accounts:
            if customer_id in self.bank_accounts[account]['owners']:
                accounts_list.append(account)
        if len(accounts_list) > 0:
            print(f'Customer ID: {customer_id}, has the following accounts: {accounts_list}')
        else:
            error = f"ERROR: Given customer ID ({customer_id}) doesn't own any accounts."
            return print(error)

    # SHOW ACCOUNT HISTORY LOG:
    def show_log(self, account_id: int) -> str | None:
        if account_id not in self.bank_accounts.keys():
            error = f"ERROR: Invalid account ({account_id}), no logs to display."
            return print(error)
        else:
            print(f"Account #{account_id} Transaction Log:")
            return Account.show_log(self.bank_accounts[account_id]["account_details"])

    # DEPOSIT TO ACCOUNT:
    def deposit(self, account_id: int, amount: int, currency: str):
        currency = currency.upper()
        if account_id not in self.bank_accounts.keys():
            error = f"ERROR: Unknown account ID ({account_id}). Can't deposit."
            return print(error)
        if amount <= 0:
            error = f"ERROR: Deposit amount ({amount}) must be a positive integer."
            return print(error)
        if currency not in self.available_currencies:
            error = f"ERROR: Currency type ({currency}) is not supported.\n" \
                    f"Available currencies: {self.available_currencies}"
            return print(error)
        if (currency != "ILS") and \
            (self.bank_accounts[account_id]['account_details'].is_foreign_currency is False):
            error = f"ERROR: Account ID ({account_id}) doesn't support foreign currency ({currency})."
            return print(error)
        else:
            if currency == "ILS":
                self.bank_accounts[account_id]['account_details'].balance[0]['ILS'] += amount
            if currency == "USD":
                self.bank_accounts[account_id]['account_details'].balance[1]['USD'] += amount
            # Execute transaction log function within Account:
            Account.log_transaction(self.bank_accounts[account_id]['account_details'], 'deposit', currency, amount)

    # WITHDRAW:
    def withdraw(self, account_id: int, amount: int, currency: str):
        currency = currency.upper()
        if account_id not in self.bank_accounts.keys():
            error = f"ERROR: Unknown account ID ({account_id}). Can't withdraw."
            return print(error)
        if amount <= 0:
            error = f"ERROR: Withdraw amount ({amount}) must be a positive integer."
            return print(error)
        if currency not in self.available_currencies:
            error = f"ERROR: Currency type ({currency}) is not supported.\n" \
                    f"Available currencies: {self.available_currencies}"
            print(error)
        if (currency != "ILS") and \
            (self.bank_accounts[account_id]['account_details'].is_foreign_currency is False):
            error = f"ERROR: Account ID ({account_id}) doesn't support foreign currency ({currency})."
            return print(error)
        if amount > self.bank_accounts[account_id]['account_details'].balance[0]['ILS'] + \
            self.bank_accounts[account_id]['account_details'].balance[1]['USD'] * self.usd_rate + \
            self.bank_accounts[account_id]['account_details'].credit_limit:
            error = f"ERROR: Your withdraw request is unsuccessful due to credit limitations. Try withdrawing less."
            return error
        else:
            if currency == "ILS":
                self.bank_accounts[account_id]['account_details'].balance[0]['ILS'] -= amount
            if currency == "USD":
                self.bank_accounts[account_id]['account_details'].balance[1]['USD'] -= amount
            # Execute transaction log function within Account:
            Account.log_transaction(self.bank_accounts[account_id]['account_details'], 'withdraw', currency, amount)


# Implement the following methods:
# transfer - transfer amount from one account to another
# convert - convert specified amount from shekels to usd or vise versa inside the account if applicable. think about edge cases!
# advanced: get cash flow per month and year - given month and year, return total sum of income and total sum of outcome to / from the account
