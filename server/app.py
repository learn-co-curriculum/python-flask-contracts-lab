#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response
app = Flask(__name__)


contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

@app.route("/contract/<int:id>")
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200
    return {"error": " Contract not found"}, 404


@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    if customer_name in customers:
        return customer_name, 204
    return {"error": "Customer not found"}, 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
