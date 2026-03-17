#!/usr/bin/env python3
from flask import Flask, jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200
    
    return jsonify({"error": "Contract not found"}), 404


@app.route('/customer/<string:customer_name>')
def get_customer(customer_name):
        if customer_name.lower() in customers:
            return "" ,204
        return jsonify({"error": "customer not found"}), 404



if __name__ == '__main__':
    app.run(port=5555, debug=True)
