#!/usr/bin/env python3
from flask import Flask, request, current_app, g, make_response, jsonify

# Sample data
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

# Initialize Flask app
app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Get contract by ID.
    
    Args:
        id: Integer - contract ID from URL
        
    Returns:
        200 with contract data if found
        404 if not found
    """
    # Search for contract with matching id
    for contract in contracts:
        if contract['id'] == id:
            # Found - return contract data with 200 status
            return make_response(jsonify(contract), 200)
    
    # Not found - return 404
    return make_response('', 404)


@app.route('/customer/<string:customer_name>')
def get_customer(customer_name):
    """
    Check if customer exists (without returning sensitive data).
    
    Args:
        customer_name: String - customer name from URL
        
    Returns:
        204 (no content) if customer exists
        404 if customer not found
    """
    # Check if customer exists (case-insensitive)
    if customer_name.lower() in customers:
        # Customer exists - return 204 with empty body (no sensitive data)
        return make_response('', 204)
    
    # Customer not found - return 404
    return make_response('', 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)