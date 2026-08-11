#!/usr/bin/env python3

from flask import Flask, make_response

# Sample contract and customer data for the lab exercise.
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """Return contract information for a matching contract ID."""
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    return {"error": "Contract not found"}, 404


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    """Confirm whether the customer exists without returning sensitive details."""
    if customer_name.lower() in [customer.lower() for customer in customers]:
        return make_response("", 204)

    return {"error": "Customer not found"}, 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
