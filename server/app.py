
from flask import Flask, jsonify

app = Flask(__name__)

# Sample contract information
contracts = [
    {"id": 1, "name": "Contract A", "value": 5000},
    {"id": 2, "name": "Contract B", "value": 8000},
    {"id": 3, "name": "Contract C", "value": 10000}
]

# Sample customer names
customers = ["John", "Sarah", "Mike"]


# CONTRACT ROUTE
# Returns contract information if the contract exists.
# Returns 404 if the contract cannot be found.

@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200

    return jsonify({"error": "Contract not found"}), 404


# CUSTOMER ROUTE
# Returns 204 if the customer exists.
# Does not reveal any customer information.
# Returns 404 if the customer cannot be found.

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return '', 204

    return jsonify({"error": "Customer not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
