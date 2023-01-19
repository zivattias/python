import psycopg2
from flask import Flask, jsonify, request
from util_methods import *

app = Flask(__name__)

_API_URL = endpoint()
_PARAMS = params()
conn = psycopg2.connect(**_PARAMS)

_RESOURCES = [
    'customers',
    'accounts'
]


@app.route('/')
def home():
    return "Bank API by Ziv"


# Get all customers' wet data (inc account_id)
# Allowed filtering by page_num, results_per_page, name, address and passport_num
@app.route('/api/v1/customers', methods=['GET'])
def get_all_customers_wet():
    results_per_page = request.args.get('rpp') or 20
    page_num = request.args.get('page') or 0
    passport_num = request.args.get('passport_num')
    name = request.args.get('name')
    address = request.args.get('address')

    if not isinstance(page_num, int) or not isinstance(results_per_page, int):
        if not str(page_num).isdigit() or not str(results_per_page).isdigit():
            return jsonify({'Error': 'Invalid page num/results per page, must be positive integers!'}), 404

    page_num, results_per_page = int(page_num), int(results_per_page)

    if request.method == 'GET':
        query = "SELECT customers.id, passport_num, fullname, address, account_id FROM customers " \
                "JOIN customers_accounts ON customers.id = customers_accounts.customer_id"

        conditions = list()
        params = list()

        if request.args.get('passport_num'):
            conditions.append("passport_num::text ILIKE %s")
            params.append(f"%{passport_num}%")

        if request.args.get('name'):
            conditions.append("fullname ILIKE %s")
            params.append(f"%{name}%")

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
                    ret_data = dictify({
                        'customer_id': {
                            item[0]: {
                                'passport_num': item[1],
                                'name': item[2],
                                'address': item[3]
                            }
                            for item in result
                        }}
                    )
                    return jsonify(ret_data), 200
                else:
                    return jsonify({'Error': 'No customer found with given filter params'}), 404


# Get a specific customer dry data (exc account-related data)
# Update a specific customer with form data - WIP
@app.route('/api/v1/customers/<int:customer_id>', methods=['GET', 'POST'])
def get_customer_dry(customer_id):
    if request.method == 'GET':
        with conn.cursor() as curs:
            query = "SELECT * FROM customers WHERE id = %s"
            curs.execute(query, (customer_id,))
            result = curs.fetchone()
            if result:
                ret_data = dictify({
                    result[0]: {
                        'passport_num': result[1],
                        'name': result[2],
                        'address': result[3]
                    }
                })
                return jsonify(ret_data), 200
            else:
                return jsonify({'Error': f'No customer found with given ID ({customer_id}).'}), 404

    if request.method == 'POST':
        with conn.cursor() as curs:
            # Update customer data
            pass


# Get specific customer's accounts data
@app.route('/api/v1/customers/<int:customer_id>/accounts')
def get_customer_accounts(customer_id):
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


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
