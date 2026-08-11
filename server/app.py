#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    """
    Fetch contract information by ID.
    Returns 200 JSON payload if found, 404 JSON error if not found.
    """
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200

    return jsonify({"error": "Contract not found"}), 404


@app.route("/customer/<customer_name>", methods=["GET"])
def check_customer(customer_name):
    """
    Verify customer existence without leaking sensitive data.
    Returns 204 Empty Body if found, 404 JSON error if not found.
    """
    if customer_name in customers:
        # 204 No Content must return an empty response body
        return make_response("", 204)

    return jsonify({"error": "Customer not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
