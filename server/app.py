#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to app"


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """
    GET /contract/<id>
    - Returns 200 OK with contract information if found.
    - Returns 404 Not Found if the contract does not exist.
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        return contract["contract_information"], 200
    return jsonify({"error": "Contract not found"}), 404


@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer(customer_name):
    """
    GET /customer/<customer_name>
    - Returns 204 No Content with an empty body if the customer exists (sensitive data protected).
    - Returns 404 Not Found if the customer does not exist.
    """
    # Case-insensitive check against the customers list
    customer_exists = any(c.lower() == customer_name.lower() for c in customers)
    
    if customer_exists:
        # 204 status requires an empty response body
        return '', 204
    
    return jsonify({"error": "Customer not found"}), 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
