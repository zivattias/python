import psycopg2
from flask import Flask, jsonify, request
from util_methods import *

app = Flask(__name__)

_API_URL = endpoint()
_PARAMS = params()
conn = psycopg2.connect(**_PARAMS)


@app.route('/')
@app.route('/home')
def home():
    return "Bank API by Ziv"


# CUSTOMERS METHODS #
# Get all customers' wet data (inc account_id)
# Allowed filtering by page_num, results_per_page, name, address and passport_num
# Add customers to db by using a POST method
@app.route('/api/v1/customers', methods=['GET', 'POST'])
def get_all_customers_wet():
    if request.method == 'GET':
        results_per_page = request.args.get('rpp') or 20
        page_num = request.args.get('page') or 0
        passport_num = request.args.get('passport_num')
        name = request.args.get('name')
        address = request.args.get('address')

        try:
            page_num, results_per_page = int(page_num), int(results_per_page)
            if page_num < 0 or results_per_page < 0:
                return jsonify({'Error': 'page num and results per page must be positive'}), 404
        except ValueError:
            return jsonify({'Error': 'page num and results per page must be integers'}), 404

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
                        }
                    })
                    return jsonify(ret_data), 200
                else:
                    return jsonify({'Error': 'No customer found with given filter params'}), 404

    if request.method == 'POST':
        if {"passport_num", "name", "address"} != request.form.keys():
            return jsonify({"Error": "Invalid form data params"}), 400

        passport_num = request.form['passport_num']
        name = request.form['name']
        address = request.form['address']

        try:
            passport_num = int(passport_num)
        except ValueError:
            return jsonify({"Error": "Passport number must be an integer"}), 400

        if not name or not address:
            return jsonify({"Error": f"To add a customer, "
                                     f"you must specify all params {passport_num, name, address}"}), 400

        query = f"INSERT INTO customers (passport_num, fullname, address)" \
                f" VALUES (%s, %s, %s)"

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (passport_num, name, address))
                if curs.rowcount == 1:
                    return jsonify({"Success": f"Added customer: {passport_num, name, address}"}), 200
                else:
                    return jsonify({'Error': 'Failed to add a customer'}), 400


# Get a specific customer dry data (exc account-related data)
# Update a specific customer with form data - WIP
@app.route('/api/v1/customers/<int:customer_id>', methods=['GET', 'PUT'])
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

    if request.method == 'PUT':
        with conn.cursor() as curs:
            if not set(request.form.keys()).issubset({"passport_num", "fullname", "address"}):
                return jsonify({"Error": "Invalid form data params"}), 400

            passport_num = request.form['passport_num']
            fullname = request.form['fullname']
            address = request.form['address']

            try:
                passport_num = int(passport_num)
            except ValueError:
                return jsonify({"Error": "Passport number must be an integer"}), 400

            conditions = list()
            params = list()

            for key in request.form.keys():
                if request.form[key]:
                    conditions.append(f"{key} = %s")
                    params.append(request.form[key]) if key != 'passport_num' \
                        else params.append(int(request.form[key]))

            query = "UPDATE customers"

            if conditions:
                query += " SET " + ", ".join(conditions) + f" WHERE id = {customer_id}"

            curs.execute(query, params)
            if curs.rowcount == 1:
                return jsonify({"Success": f"Updated customer {customer_id}:"
                                           f" {passport_num, fullname, address}"}), 200
            else:
                return jsonify({'Error': 'Failed to update a customer'}), 400


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
    app.run(port=3000)
