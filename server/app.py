#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def get_contract(id):
    contract = next((item for item in contracts if item['id'] == id), None)
    if contract:
        return "This contract is for John and building a shed",200
    else:
        return "Contract not found",404

@app.route('/customer/<string:name>')
def get_customer(name):
    if name in customers:
        return "Customer found, no information (it's sensitive!)",204
    else:
        return "Customer not found",404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
