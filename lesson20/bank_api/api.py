import psycopg2
from flask import Flask, jsonify, request
from util_methods import *
from datetime import datetime

app = Flask(__name__)

_PARAMS = params()
conn = psycopg2.connect(**_PARAMS)


@app.route('/')
@app.route('/home')
def home():
    return "Bank API by Ziv Attias"


# CUSTOMERS METHODS #

# Get all customers' wet data (inc account_id)
# Allowed filtering by page_num, results_per_page, fullname, address and passport_num
# Add customers to db by using a POST method
@app.route('/api/v1/customers', methods=['GET', 'POST'])
def get_all_customers_wet():
    if request.method == 'GET':
        results_per_page = request.args.get('rpp') or 20
        page_num = request.args.get('page') or 0
        passport_num = request.args.get('passport_num')
        fullname = request.args.get('fullname')
        address = request.args.get('address')

        try:
            page_num, results_per_page = int(page_num), int(results_per_page)
            if page_num < 0 or results_per_page < 0:
                return jsonify({'Error': 'page num and results per page must be positive'}), 404
        except ValueError:
            return jsonify({'Error': 'page num and results per page must be integers'}), 404

        query = "SELECT customers.id, passport_num, fullname, address, account_id FROM customers " \
                "LEFT JOIN customers_accounts ON customers.id = customers_accounts.customer_id"

        conditions = list()
        params = list()

        if request.args.get('passport_num'):
            conditions.append("passport_num::text ILIKE %s")
            params.append(f"%{passport_num}%")

        if request.args.get('fullname'):
            conditions.append("fullname ILIKE %s")
            params.append(f"%{fullname}%")

        if request.args.get('address'):
            conditions.append("address ILIKE %s")
            params.append(f"%{address}%")

        offset = page_num * results_per_page - results_per_page if page_num != 0 else 0
        limit = results_per_page

        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += f" LIMIT {limit} OFFSET {offset}"

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, params)
                result = curs.fetchall()
                if result:
                    ret_data = dict()
                    for item in result:
                        if item[1] not in ret_data:
                            ret_data[item[1]] = {
                                "customer_id": item[0],
                                "fullname": item[2],
                                "address": item[3],
                                "account_id": [item[4]]
                            }
                        else:
                            ret_data[item[1]]['account_id'].append(item[4])

                    ret_data = dictify({
                        "passport_num": ret_data
                    })
                    return jsonify(ret_data), 200
                else:
                    return jsonify({'Error': 'No customer found with given filter params'}), 404

    if request.method == 'POST':
        if {"passport_num", "fullname", "address"} != request.form.keys():
            return jsonify({"Error": "Invalid form data params"}), 400

        passport_num = request.form['passport_num']
        fullname = request.form['fullname']
        address = request.form['address']

        try:
            passport_num = int(passport_num)
        except ValueError:
            return jsonify({"Error": "Passport number must be an integer"}), 400

        if not fullname or not address:
            return jsonify({"Error": f"To add a customer, "
                                     f"you must specify all params {passport_num, fullname, address}"}), 400

        query = f"INSERT INTO customers (passport_num, fullname, address)" \
                f" VALUES (%s, %s, %s)"

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (passport_num, fullname, address))
                if curs.rowcount == 1:
                    return jsonify({"Success": f"Added customer: {passport_num, fullname, address}"}), 200
                else:
                    return jsonify({'Error': 'Failed to add a customer'}), 400


# Get a specific customer dry data (exc account-related data)
# Update a specific customer with form data params
# Delete specific customer from db
@app.route('/api/v1/customers/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_customer(customer_id):
    if request.method == 'GET':
        with conn:
            with conn.cursor() as curs:
                query = "SELECT * FROM customers WHERE id = %s"
                curs.execute(query, (customer_id,))
                result = curs.fetchone()
                if result:
                    ret_data = dictify({
                        result[0]: {
                            'passport_num': result[1],
                            'fullname': result[2],
                            'address': result[3]
                        }
                    })
                    return jsonify(ret_data), 200
                else:
                    return jsonify({'Error': f'No customer found with given ID ({customer_id}).'}), 404

    if request.method == 'PUT':
        if not set(request.form.keys()).issubset({'passport_num', 'address', 'fullname'}):
            return jsonify({"Error": "Invalid form data provided"}), 400

        with conn:
            with conn.cursor() as curs:
                conditions = list()
                params = list()

                for key in request.form.keys():
                    conditions.append(f"{key} = %s")
                    if key != 'passport_num':
                        params.append(request.form[key])
                    else:
                        try:
                            int(request.form[key])
                        except ValueError:
                            return jsonify({"Error": "Passport number must be an integer"}), 400
                        params.append(int(request.form[key]))

                query = "UPDATE customers"

                if conditions:
                    query += " SET " + ", ".join(conditions) + f" WHERE id = {customer_id}"

                curs.execute(query, params)
                if curs.rowcount == 1:
                    return jsonify({"Success": f"Updated customer {customer_id}:"
                                               f" {params}"}), 200
                else:
                    return jsonify({'Error': 'Invalid customer ID provided'}), 400

    if request.method == 'DELETE':
        with conn:
            with conn.cursor() as curs:
                query = "SELECT account_id FROM customers_accounts WHERE customer_id = %s"
                curs.execute(query, (customer_id,))
                if curs.rowcount > 0:
                    account_ids = [item[0] for item in curs.fetchall()]
                    return jsonify({"Error": f"Customer possesses account(s): {account_ids}, delete them first"}), 400
                else:
                    query = "DELETE FROM customers WHERE id = %s"
                    curs.execute(query, (customer_id,))
                    if curs.rowcount == 1:
                        return jsonify({"Success": f"Deleted customer {customer_id}"}), 200
                    else:
                        return jsonify({"Error": f"Invalid customer ID {customer_id}"}), 400


# Get specific customer's accounts data
@app.route('/api/v1/customers/<int:customer_id>/accounts')
def get_customer_accounts(customer_id):
    with conn:
        with conn.cursor() as curs:
            query = f"SELECT id, account_num, max_limit, balance FROM accounts WHERE id =" \
                    f" (SELECT account_id FROM customers_accounts WHERE customer_id = {customer_id});"
            curs.execute(query, (customer_id,))
            result = curs.fetchall()
            if result:
                ret_data = dictify({
                    'account_id': {
                        item[0]: {
                            'account_num': item[1],
                            'max_limit': f"{item[2]:,d}",
                            'balance': f"{item[3]:,d}"
                        }
                        for item in result
                    }
                })
                return jsonify(ret_data), 200
            else:
                return jsonify({'Error': f'No accounts found for customer with given ID ({customer_id}).'}), 404


# ACCOUNTS METHODS #

# Get specific account data
@app.route('/api/v1/accounts/<int:account_id>', methods=['GET', 'DELETE'])
def get_account_by_id(account_id):
    if request.method == 'GET':
        with conn:
            with conn.cursor() as curs:
                query = "SELECT * FROM accounts WHERE account_num = %s"
                curs.execute(query, (account_id,))
                result = curs.fetchall()
                if result:
                    ret_data = dictify({
                        item[1]: {
                            "account_id": item[0],
                            "max_limit": item[2],
                            "balance": item[3]
                        }
                        for item in result
                    })
                    return jsonify(ret_data), 200
                else:
                    return jsonify({"Error": f"Invalid account ID given {account_id}"}), 400

    if request.method == 'DELETE':
        with conn:
            with conn.cursor() as curs:
                query = "SELECT * FROM customers_accounts WHERE account_id = %s"
                curs.execute(query, (account_id,))
                if curs.rowcount == 0:
                    return jsonify({"Error": f"Invalid account ID {account_id}"})
                query = "DELETE FROM customers_accounts WHERE account_id = %s"
                curs.execute(query, (account_id,))
                if curs.rowcount > 0:
                    query = "DELETE FROM accounts WHERE id = %s"
                    curs.execute(query, (account_id,))
                    if curs.rowcount > 0:
                        return jsonify({"Success": f"Account ID {account_id} was deleted"})
                else:
                    return jsonify({"Error": "Database error"}), 500


# Get all accounts data;
# Filtering by balance and/or max_limit allowed.
# Create a new account given account_num, max_limit & account owners (customer_ids) in form data
@app.route('/api/v1/accounts', methods=['GET', 'POST'])
def get_all_accounts():
    if request.method == 'GET':
        balance = request.args.get('balance')
        max_limit = request.args.get('max_limit')

        conditions = list()
        params = list()

        if balance:
            conditions.append("balance = %s")
            params.append(balance)

        if max_limit:
            conditions.append("max_limit = %s")
            params.append(max_limit)

        query = "SELECT * FROM accounts"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, params)
                result = curs.fetchall()
                if not result:
                    return jsonify({"Error": "No accounts found for given query params"}), 404
                ret_data = dictify({
                    item[1]: {
                        "account_id": item[0],
                        "max_limit": item[2],
                        "balance": item[3]
                    }
                    for item in result
                })
                return jsonify(ret_data), 200

    if request.method == 'POST':
        account_num = request.form.get('account_num')
        max_limit = request.form.get('max_limit')
        base_owners = request.form.get('account_owners').strip()
        if base_owners.count(',') > 0:
            flag = True
            try:
                int(base_owners.replace(' ', '').replace(',', ''))
            except ValueError:
                return jsonify({"Error": "Account owner IDs must be integers"}), 400
        else:
            flag = False
            try:
                int(base_owners)
            except ValueError:
                return jsonify({"Error": "Account owner ID must be an integer"}), 400

        account_owners = base_owners.replace(' ', '').split(',') if flag else list(base_owners)

        account_creation = 'INSERT INTO accounts (account_num, max_limit, balance) VALUES (%s, %s, 0)'
        account_connection = 'INSERT INTO customers_accounts (account_id, customer_id) VALUES (%s, %s)'

        with conn:
            with conn.cursor() as curs:
                curs.execute(account_creation, (account_num, max_limit))
                if curs.rowcount == 1:
                    curs.execute("SELECT last_value FROM accounts_id_seq")
                    account_id = curs.fetchone()[0]
                    counter = 0
                    for owner in account_owners:
                        curs.execute(account_connection, (account_id, owner))
                        counter += 1 if curs.rowcount == 1 else 0
                    if counter == len(account_owners):
                        return jsonify({"Success": f"Account {account_id} created:"
                                                   f" {account_num, max_limit, account_owners}"})
                else:
                    return jsonify({"Error": "Couldn't create account with given form data"}), 400


# Deposit to account - amount & initiator passport_num in form data
@app.route('/api/v1/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
    if request.method == 'POST':
        account_id = account_id
        amount = request.form.get('amount')
        initiated_by = request.form.get('passport_num')
        if not initiated_by or not deposit:
            return jsonify({"Error": "Can't complete deposit without amount and passport number"})

        try:
            amount = int(amount)
            initiated_by = int(initiated_by)
            if amount <= 0:
                return jsonify({"Error": "Deposit amount must be positive"})
        except ValueError:
            return jsonify({"Error": "Deposit amount & passport number must be integers"})

        query = "SELECT customers.passport_num FROM customers_accounts " \
                "LEFT JOIN customers ON customers_accounts.customer_id = customers.id WHERE account_id = %s"
        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (account_id,))
                valid_passports = [num[0] for num in curs.fetchall()]
                if initiated_by not in valid_passports:
                    return jsonify({"Error": f"Invalid passport number {initiated_by} for account {account_id}"})
                query = "SELECT id FROM customers WHERE passport_num = %s"
                curs.execute(query, (initiated_by,))
                customer_id = curs.fetchone()[0]
                curs.execute(f"INSERT INTO transactions (trans_type, ts, initiator_id) "
                             f"VALUES ('deposit', '{datetime.utcnow()}', {customer_id})")
                curs.execute("SELECT last_value FROM transactions_id_seq")
                transaction_id = int(curs.fetchone()[0])
                if curs.rowcount == 1:
                    curs.execute("INSERT INTO transactions_accounts (account_role, transaction_id, account_id)"
                                 f" VALUES ('self', {transaction_id}, {account_id})")
                    curs.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE id = {account_id}")
                    if curs.rowcount == 1:
                        return jsonify({"Success": f"Transaction {transaction_id} (deposit) for "
                                                   f"account {account_id} has been completed!"})


# Withdraw from account - amount & initiator passport_num in form data
@app.route('/api/v1/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
    if request.method == 'POST':
        account_id = account_id
        amount = request.form.get('amount')
        initiated_by = request.form.get('passport_num')
        if not initiated_by or not deposit:
            return jsonify({"Error": "Can't complete withdrawal without amount and passport number"})

        try:
            amount = int(amount)
            initiated_by = int(initiated_by)
            if amount <= 0:
                return jsonify({"Error": "Withdrawal amount must be positive"})
        except ValueError:
            return jsonify({"Error": "Withdrawal amount & passport number must be integers"})

        query = "SELECT customers.passport_num FROM customers_accounts " \
                "LEFT JOIN customers ON customers_accounts.customer_id = customers.id WHERE account_id = %s"
        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (account_id,))
                valid_passports = [num[0] for num in curs.fetchall()]
                if initiated_by not in valid_passports:
                    return jsonify({"Error": f"Invalid passport number {initiated_by} for account {account_id}"})
                curs.execute(f"SELECT balance, max_limit FROM accounts WHERE id = {account_id}")
                balance, max_limit = curs.fetchone()
                if balance - amount <= max_limit:
                    return jsonify({"Error": "Insufficient credit for provided amount"})
                else:
                    query = "SELECT id FROM customers WHERE passport_num = %s"
                    curs.execute(query, (initiated_by,))
                    customer_id = curs.fetchone()[0]
                    curs.execute(f"INSERT INTO transactions (trans_type, ts, initiator_id) "
                                 f"VALUES ('withdraw', '{datetime.utcnow()}', {customer_id})")
                    curs.execute("SELECT last_value FROM transactions_id_seq")
                    transaction_id = int(curs.fetchone()[0])
                    if curs.rowcount == 1:
                        curs.execute("INSERT INTO transactions_accounts (account_role, transaction_id, account_id)"
                                     f" VALUES ('self', {transaction_id}, {account_id})")
                        curs.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE id = {account_id}")
                        if curs.rowcount == 1:
                            return jsonify({"Success": f"Transaction {transaction_id} (withdrawal) for "
                                                       f"account {account_id} has been completed!"})


# Transfer from one account to another - amount, to_account, passport_num in form data
@app.route('/api/v1/accounts/<int:account_id>/transfer', methods=['POST'])
def transfer(account_id):
    if request.method == 'POST':
        from_account = account_id
        to_account = request.form.get('to_account')
        amount = request.form.get('amount')
        passport_num = request.form.get('passport_num')

        if not to_account or not amount or not passport_num:
            return jsonify({"Error": "Can't execute transfer without all fields filled"}), 400

        try:
            amount, passport_num, to_account = int(amount), int(passport_num), int(to_account)
            if amount <= 0:
                return jsonify({"Error": "Transfer amount is less than or equals to 0"}), 400
        except ValueError:
            return jsonify({"Error": "One or more fields are not integers"}), 400

        with conn:
            with conn.cursor() as curs:
                query = "SELECT * FROM accounts WHERE id = %s"
                curs.execute(query, (to_account,))
                if curs.rowcount == 0:
                    return jsonify({"Error": f"Account ID {to_account} not found"})
                query = "SELECT customers.passport_num FROM customers_accounts " \
                        "LEFT JOIN customers ON customers_accounts.customer_id = customers.id WHERE account_id = %s"
                curs.execute(query, (from_account,))
                valid_passports = [num[0] for num in curs.fetchall()]
                if passport_num not in valid_passports:
                    return jsonify({"Error": f"Invalid passport number {passport_num} for account {from_account}"})
                curs.execute(f"SELECT balance FROM accounts WHERE id = {from_account}")
                balance = curs.fetchone()[0]
                if balance < amount:
                    return jsonify({"Error": "Insufficient funds in originating account"})

                query = "SELECT id FROM customers WHERE passport_num = %s"
                curs.execute(query, (passport_num,))
                customer_id = curs.fetchone()[0]
                curs.execute("INSERT INTO transactions(trans_type, ts, initiator_id) "
                             f"VALUES ('transfer', '{datetime.now()}', {customer_id})")

                curs.execute("SELECT last_value FROM transactions_id_seq")
                trans_id = curs.fetchone()[0]

                curs.execute("INSERT INTO transactions_accounts(account_role, account_id, transaction_id)"
                             f"VALUES ('receiver', {to_account}, {trans_id})")
                curs.execute("INSERT INTO transactions_accounts(account_role, account_id, transaction_id)"
                             f"VALUES ('sender', {from_account}, {trans_id})")

                curs.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE id = {from_account}")
                curs.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE id = {to_account}")
                return jsonify({"Success": "Transfer completed"}), 200


if __name__ == '__main__':
    app.run(port=3000)
