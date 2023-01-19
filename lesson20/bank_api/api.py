from util_methods import *
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

_API_URL = endpoint()
_PARAMS = params()
conn = psycopg2.connect(**_PARAMS)


@app.route('/')
def home():
    return "Bank API"


@app.route('/api/v1/customers', methods=['GET'])
def get_all_customers():
    if request.method == 'GET':
        with conn:
            with conn.cursor() as curs:
                query = "SELECT customers.id, passport_num, fullname, address, account_id FROM customers " \
                        "JOIN customers_accounts ON customers.id = customers_accounts.customer_id"
                curs.execute(query)
                result = curs.fetchall()
                ret_data = {
                    'data': {
                        'customer_id': {
                            item[0]: {
                                'passport_num': item[1],
                                'name': item[2],
                                'address': item[3]
                            }
                            for item in result
                        }
                    }
                }
                return jsonify(ret_data)


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
