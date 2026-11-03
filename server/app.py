#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, jsonify

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"}
]
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Looks up a contract by id in the contracts array.
    200 + contract info if found, 404 if not found.
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract is None:
        return make_response(jsonify({"error": "Contract not found"}), 404)
    return make_response(jsonify(contract), 200)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """
    Looks up a customer by name in the customers array.
    Customer data is sensitive, so a found customer returns
    204 (No Content) with an empty body — just confirmation
    they exist, no details. 404 if not found.
    """
    if customer_name in customers:
        return make_response('', 204)
    return make_response(jsonify({"error": "Customer not found"}), 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)