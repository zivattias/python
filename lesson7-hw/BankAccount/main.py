from bank import *

if __name__ == '__main__':
    # Initialize bank:
    bank = Bank('Cupertino Bank', '001')

    # Add 3 sample users to bank:
    bank.add_user(700801, 'Ziv Attias', '34 HaTekuma St, Tel Aviv-Jaffa', '052-8039540', 'ziv.attias7@gmail.com')
    bank.add_user(700802, 'Noa Gilboa', '34 HaTekuma St, Tel Aviv-Jaffa', '054-4444444', 'noa.gilboa@gmail.com')
    bank.add_user(700803, 'Dvir Stern', '4 Michaelangelo St, Tel-Aviv-Jaffa', '052-2222222', 'dvir.stern@gmail.com')

    # Connect 3 users to 2 accounts:
    bank.create_account(700801, 1001, 10000, True)  # Will create Ziv's account (1001)
    bank.create_account(700802, 1001, 10000, True)  # Will add Noa to Ziv's account (1001)
    bank.create_account(700803, 1002, 5000, False)  # Will create Dvir's account (1002)
    bank.create_account(700804, 1001, 5000, True)  # Error: Customer ID (700804) doesn't exist

    # Display account's owners:
    bank.display_account_owners(1001)  # - The account has multiple owners (Ziv, Noa), should display accordingly
    bank.display_account_owners(1002)  # - The account has one owner (Dvir)
    bank.display_account_owners(1003)  # - Error: The account doesn't exist

    # Display user's accounts:
    bank.display_owner_accounts(700801)  # - The owner (Ziv) has account 1001
    bank.display_owner_accounts(700802)  # - The owner (Noa) has account 1001
    bank.display_owner_accounts(700803)  # - The owner (Dvir) has account 1002
    bank.display_owner_accounts(700804)  # - Error: The customer doesn't exist, no accounts to display

    # Deposits:
    bank.deposit(1001, 10_000, "ILS")   # - Deposit 10,000 ILS to account 1001
    bank.deposit(1002, 5_000, "ILS")    # - Deposit 5,000 ILS to account 1002
    bank.deposit(1001, 200, "USD")      # - Deposit 200 USD to account 1001
    bank.deposit(1002, 200, "USD")      # - Error: Account 1002 doesn't support foreign currency
    bank.deposit(1003, 1, "ILS")        # - Error: Account 1003 doesn't exist
    bank.deposit(1001, -1, "ILS")       # - Error: Amount must be > 0
    bank.deposit(1001, 1, "EUR")        # - Error: Currency 'EUR' is unsupported by bank

    # Withdrawals:
    bank.withdraw(1001, 200, "USD")     # - Withdraw 200 USD from account 1001

    # Show balances of accounts:
    print(bank.bank_accounts[1001]['account_details'])  # - Will display account details for account 1001.
    print(bank.bank_accounts[1002]['account_details'])  # - Will display account details for account 1002.

    # Show log of accounts:
    bank.show_log(1001) # - Displays logs for account 1001.
    bank.show_log(1002) # - Displays logs for account 1002.
    bank.show_log(1003) # - Error: Unknown account, won't display.



