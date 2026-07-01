#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

# Create the Flask application instance
app = Flask(__name__)

# List of available contracts
contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed"
    },
    {
        "id": 2,
        "contract_information": "This contract is for a deck for a buisiness"
    },
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car"
    }
]

# List of customers
customers = ["bob", "bill", "john", "sarah"]

# Contract Route

@app.route("/contract/<int:id>")
def get_contract(id):
    # Find the contract with the matching ID
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract:
        return contract["contract_information"], 200

    return "", 404

# Customer Route

@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    if customer_name in customers:
        return "", 204

    return "", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
