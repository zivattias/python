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
    return float(result[0])


def get_max_limit(account_num: int) -> float:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT max_limit FROM accounts WHERE account_num = {account_num}")
            result = curs.fetchone()
    conn.close()
    return float(result[0])


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
            account_nums = list()
            for account_id in accounts_ids:
                curs.execute(f"SELECT account_num FROM accounts WHERE id = {account_id[0]}")
                account_nums.append(curs.fetchall()[0][0])
    conn.close()
    return account_nums

def get_customer_id_by_passport(num: int) -> int:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT id FROM customers WHERE passport_num = {num}")
            customer_id = curs.fetchone()
    conn.close()
    return customer_id[0]

def get_account_id_by_account_num(num: int) -> int:
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute(f"SELECT id FROM accounts WHERE account_num = {num}")
            account_id = curs.fetchone()
    conn.close()
    return account_id[0]


def transfer(from_account: int, to_account: int, amount: int, initiated_by: int) -> bool:
    if (not (validate_account_num(from_account) and validate_account_num(to_account))) or (
        from_account not in get_account_by_passport(initiated_by)) or (
        amount > (get_balance(from_account) + get_max_limit(from_account))):
        return False

    with psycopg2.connect(**params) as conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO transactions(trans_type, ts, initiator_id) "
                         f"VALUES ('transfer', '{datetime.now()}', {get_customer_id_by_passport(initiated_by)})")
            curs.execute("commit;")
            curs.execute("SELECT currval('transactions_id_seq'::regclass);")
            trans_id = curs.fetchone()[0]
            curs.execute("INSERT INTO transactions_accounts(account_role, account_id, transaction_id)"
                         f"VALUES ('receiver', {get_account_id_by_account_num(to_account)}, {trans_id})")
            curs.execute("INSERT INTO transactions_accounts(account_role, account_id, transaction_id)"
                         f"VALUES ('sender', {get_account_id_by_account_num(from_account)}, {trans_id})")
            curs.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account_num = {from_account}")
            curs.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE account_num = {to_account}")
    conn.close()
    return True


if __name__ == '__main__':
    print(transfer(1, 2, 4000000, 123456789))
    print(transfer(1, 2, 100000, 123456789))
