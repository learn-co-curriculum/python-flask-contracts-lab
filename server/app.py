#!/usr/bin/env python3

from flask import Flask, request,jsonify

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


@app.route('/contracts/<int:id>', methods=['GET'])
def get_contracts(id):
    for contract in contracts:
        if contract["id"] == id:
         return jsonify({"contract fouund, give information": contract}, 200)
          
    return jsonify({"error": "Contract not found"}, 404)

@app.route("/customers/<string:name>", methods=['GET'])
def get_customers(name):
    if name in customers:
        return({"customers found, give information": customers}, 200)
    else:
        return jsonify({"error": "Customer not found"}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
