#!/usr/bin/env python3

from flask import Flask, jsonify, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},
             {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
             {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """Return contract details if ID exists, else 404."""
    contract = next((item for item in contracts if item["id"] == id), None)
    if contract:
        return jsonify(contract), 200
    return jsonify({"error": "Contract not found"}), 404


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    """Return 204 No Content if customer exists, else 404."""
    if customer_name.lower() in [name.lower() for name in customers]:
        return '', 204
    return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)%555
