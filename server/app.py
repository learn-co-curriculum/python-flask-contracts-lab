from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Sample mock data array for contracts
contracts = [
    {"id": 1, "contractor_name": "Acme Corp", "status": "Active", "value": 15000},
    {"id": 2, "contractor_name": "BuildIt LLC", "status": "Pending", "value": 8500},
]

# Sample mock array for customers
customers = ["Alice Corp", "Bob Industries", "Charlie Tech"]


@app.route("/contract/<id>", methods=["GET"])
def get_contract(id):
    """
    Route: /contract/<id>
    - Returns 200 + Contract Data if contract ID matches an entry in the list.
    - Returns 404 if contract ID does not exist.
    """
    # Convert string parameter to integer for comparison
    try:
        contract_id = int(id)
    except ValueError:
        return jsonify({"error": "Contract not found"}), 404

    for contract in contracts:
        if contract["id"] == contract_id:
            return jsonify(contract), 200

    return jsonify({"error": "Contract not found"}), 404


@app.route("/customer/<customer_name>", methods=["GET"])
def check_customer(customer_name):
    """
    Route: /customer/<customer_name>
    - Returns 204 No Content (empty body) if customer exists.
    - Returns 404 Not Found if customer does not exist.
    """
    if customer_name in customers:
        # HTTP 204 requires an empty string response body
        return make_response("", 204)

    return jsonify({"error": "Customer not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
