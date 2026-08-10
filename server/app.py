#!/usr/bin/env python3

from flask import Flask, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:contract_id>')
def contract_info(contract_id):
    contract = next((c for c in contracts if c['id'] == contract_id), None)
    if contract is None:
        return make_response('', 404)
    return contract['contract_information'], 200

@app.route('/customer/<customer_name>')
def customer_info(customer_name):
    if customer_name not in customers:
        return make_response('', 404)
    return make_response('', 204)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
