# WIP

from util_methods import *
import psycopg2
from datetime import datetime

params = get_config()

def get_balance(account_num: int) -> float:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT balance FROM accounts WHERE account_num = {account_num}")
            result = curs.fetchone()
    conn.close()
    return float(result)


def get_max_limit(account_num: int) -> float:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT max_limit FROM accounts WHERE account_num = {account_num}")
            result = curs.fetchone()
    conn.close()
    return float(result)


def validate_account_num(account_num: int) -> bool:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT exists (SELECT account_num FROM accounts"
                         f" WHERE account_num = {account_num} LIMIT 1)")
            result = curs.fetchone()
    conn.close()
    return result


def get_account_by_passport(num: int) -> list:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT account_id FROM customers_accounts WHERE customer_id = "
                         f"(SELECT id FROM customers WHERE passport_num = {num})")
            accounts_ids = curs.fetchall()
    conn.close()
    return [account[0] for account in accounts_ids]

# from account is account num whereas get_accounbt_by_passport returns account_id

def transfer(from_account: int, to_account: int, amount: int, initiated_by: int) -> bool:
    if (not (validate_account_num(from_account) and validate_account_num(to_account))) or \
       (from_account not in get_account_by_passport(initiated_by)) or \
       (amount > (get_balance(from_account) + get_max_limit(from_account))):
        return False

    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO transactions(trans_type, ts, initiator_id) "
                         f"VALUES ('transfer', {datetime.now()}, {initiated_by}")
            trans_id = curs.execute("currval(pg_get_serial_sequence('transactions', 'id'))")
            curs.execute("INSERT INTO transactions_accounts(account_role, transaction_id, account_id)"
                         f"VALUES ('receiver', {trans_id}, {to_account}")
            curs.execute("INSERT INTO transactions_accounts(account_role, transaction_id, account_id)"
                         f"VALUES ('sender', {trans_id}, {from_account}")
            curs.execute(f"UPDATE accounts SET balance -= {amount} WHERE account_num = {from_account}")
            curs.execute(f"UPDATE accounts SET balance += {amount} WHERE account_num = {to_account}")
    conn.close()
    return True

if __name__ == '__main__':
    print(transfer(1, 2, 4000000, 123456789))
    print(transfer(1, 2, 100000, 123456789))