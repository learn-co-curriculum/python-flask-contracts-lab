#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response,jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """
    Look up a contract by its numeric id.
    - If found: return the contract data with a 200 response.
    - If not found: return a 404 response.
    """
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract is None:
        return make_response(jsonify({"error": "Contract not found"}), 404)

    return make_response(contract["contract_information"], 200)


@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer(customer_name):
    """
    Check whether a customer exists by name.
    - If found: return a 204 response (no body) — data is sensitive,
      so we only confirm existence, we don't leak details.
    - If not found: return a 404 response.
    """
    if customer_name in customers:
        return make_response('', 204)

    return make_response(jsonify({"error": "Customer not found"}), 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
