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
                curs.execute("SELECT * FROM customers")
                result = curs.fetchall()
                ret_data = list()
                for item in result:
                    query = f"SELECT account_id FROM customers_accounts WHERE customer_id = %s"
                    curs.execute(query, (item[0],))
                    account_id = curs.fetchone()
                    item_dict = {
                        'id': item[0],
                        'passport_num': item[1],
                        'fullname': item[2],
                        'address': item[3],
                        'account_id': account_id[0]
                    }
                    ret_data.append(item_dict)
    return jsonify(ret_data)


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
