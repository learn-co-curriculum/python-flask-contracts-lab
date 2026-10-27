#!/usr/bin/env python3

from flask import Flask, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route("/contract/<int:contract_id>")
def get_contract(contract_id):
    for contract in contracts:
        if contract["id"] == contract_id:
            return contract["contract_information"], 200

    return "Contract not found", 404


@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return make_response("", 204)

    return make_response("Customer not found", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
