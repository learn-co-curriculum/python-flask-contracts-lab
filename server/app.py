#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

# Return contract information when the contract ID exists.
@app.route('/contract/<int:id>')
def contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    # Return 404 when the contract ID does not exist.
    return "Contract not found", 404


# Confirm that a customer exists without exposing sensitive information.
@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name in customers:
        # 204 means the request succeeded but contains no response body.
        return "", 204

    # Return 404 when the customer cannot be found.
    return "Customer not found", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
