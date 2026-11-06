#!/usr/bin/env python3

from flask import Flask, jsonify

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route("/customers")
def customer_names():
    return jsonify(customers)


@app.route("/contract/<int:contract_id>")
def get_contract(contract_id):
    """Return contract details only when the requested contract exists."""
    contract = next((item for item in contracts if item["id"] == contract_id), None)
    if contract is None:
        return "", 404
    return contract["contract_information"], 200


@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    """Confirm a customer exists without disclosing sensitive information."""
    if customer_name not in customers:
        return "", 404
    return "", 204


if __name__ == "__main__":
    app.run(port=5555, debug=True)
