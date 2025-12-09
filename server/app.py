#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract(id):
    for contract in contracts:
        if contract['id'] == id:
            status_code = 200
            return make_response(contract["contract_information"], status_code)
        
    return make_response('Contract not found.', 404)

@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name in customers:
        return make_response('Customer Found', 204)
    else:
        return make_response('Customer not found.', 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
