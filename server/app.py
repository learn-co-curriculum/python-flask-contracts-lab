#!/usr/bin/env python3
from flask import Flask, jsonify


contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)

@app.route('/')
def index():
    return 'Contract API is running. Try /contract/1 or /customers/name'
    

@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200
    return '', 404

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name.lower() in [c.lower() for c in customers]:
        return '', 204
    return '', 404

if __name__ == '__main__':
    print(app.url_map)
    app.run(port=5555, debug=True)