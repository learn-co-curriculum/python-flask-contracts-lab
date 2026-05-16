from flask import Flask, jsonify, Response

# Create Flask application instance
app = Flask(__name__)

# Mock contract data
contracts = [
    {
        "id": 1,
        "title": "Website Development",
        "value": 5000
    },
    {
        "id": 2,
        "title": "Mobile App Project",
        "value": 12000
    }
]

# Mock customer data
customers = [
    {
        "name": "alice"
    },
    {
        "name": "bob"
    }
]


# -----------------------------------
# Home Route
# -----------------------------------
# Confirms application is running
@app.route("/")
def home():
    return "Flask Contracts Lab Running!"


# -----------------------------------
# Contract Route
# -----------------------------------
# Returns contract information if ID exists
# Returns 404 if contract is not found
@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):

    # Search contracts list for matching ID
    contract = next(
        (contract for contract in contracts if contract["id"] == id),
        None
    )

    # Return contract data with success response
    if contract:
        return jsonify(contract), 200

    # Return error if contract does not exist
    return jsonify({
        "error": "Contract not found"
    }), 404


# -----------------------------------
# Customer Route
# -----------------------------------
# Returns 204 No Content if customer exists
# Returns 404 if customer is not found
@app.route("/customer/<string:customer_name>", methods=["GET"])
def get_customer(customer_name):

    # Search customer list by name
    customer = next(
        (customer for customer in customers if customer["name"] == customer_name),
        None
    )

    # 204 responses should contain no body
    if customer:
        return Response(status=204)

    # Return error if customer does not exist
    return jsonify({
        "error": "Customer not found"
    }), 404


# Run Flask development server
if __name__ == "__main__":
    app.run(debug=True)