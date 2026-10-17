#!/usr/bin/env python3

from flask import Flask, jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},
             {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route("/contract/<int:contract_id>", methods=["GET"])
def get_contract(contract_id):
    contract = next((c for c in contracts if c["id"] == contract_id), None)
    if contract:
        return contract["contract_information"]
    else:
        return jsonify({"error": "Contract not found"}), 404



@app.route("/customer/<string:customer_name>", methods=["GET"])
def get_customer(customer_name):
    if customer_name in customers:
        return "", 204
    else:
        return jsonify({"error": "Customer not found"}), 404
if __name__ == '__main__':
    app.run(port=5555, debug=True)
