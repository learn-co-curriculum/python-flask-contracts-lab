#!/usr/bin/env python3
from flask import Flask, request, current_app, g, make_response

# Sample contract data: each contract has a unique id and its info
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

# Sample customer data: just names, since customer data is sensitive
# and should not be returned in the response body
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Look up a contract by its id.
    - If found, return the contract information with a 200 response.
    - If not found, return a 404 response.
    """
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200
    return "Contract not found", 404


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """
    Look up a customer by name.
    - If found, confirm existence with a 204 response and no body
      (customer data is sensitive, so we don't return any details).
    - If not found, return a 404 response.
    """
    if customer_name in customers:
        return "", 204
    return "Customer not found", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
