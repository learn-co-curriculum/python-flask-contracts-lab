"""
This app defines two routes:
1. /contract/<id>           -> 200 if contract found, 404 if not
2. /customer/<customer_name> -> 204 if customer exists, 404 if not
"""

from flask import Flask, jsonify, make_response

# Create the Flask app
app = Flask(__name__)

# --- Demo data ---
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisness"},  
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]

customers = ["bob", "bill", "john", "sarah"]


# --- Routes section ---
@app.get("/contract/<int:contract_id>")
def get_contract(contract_id):
    """Return contract details by ID or 404 if not found."""
    contract = next((c for c in contracts if c["id"] == contract_id), None)
    if contract:
        return jsonify(contract), 200
    else:
        return jsonify({"error": "Contract not found"}), 404


@app.get("/customer/<customer_name>")
def get_customer(customer_name):
    """Return 204 if customer exists, or 404 if not."""
    name = customer_name.strip().lower()
    if name in customers:
        return make_response(("", 204))
    else:
        return jsonify({"error": "Customer not found"}), 404


# --- Run app ---
if __name__ == "__main__":
    app.run(port=5555, debug=True)