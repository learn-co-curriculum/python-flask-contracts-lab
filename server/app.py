
#!/usr/bin/env python3

from flask import Flask, make_response

# Initialize Flask application
app = Flask(__name__)

# Sample contract records
contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed"
    },
    {
        "id": 2,
        "contract_information": "This contract is for a deck for a buisiness"
    },
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car"
    }
]

# Sample customer records
customers = ["bob", "bill", "john", "sarah"]


# Home route
@app.route('/')
def home():
    return "Welcome to the Contracts Management API!", 200


# Contract route
@app.route('/contract/<int:id>')
def get_contract(id):
    # Search for the requested contract
    contract = next(
        (item for item in contracts if item["id"] == id),
        None
    )

    # Return contract information if found
    if contract:
        return make_response(contract["contract_information"], 200)

    # Return 404 if contract does not exist
    return make_response({"error": "Contract not found"}, 404)


# Customer route
@app.route('/customer/<string:customer_name>')
def get_customer(customer_name):
    # Check whether the customer exists
    if customer_name.lower() in customers:

        # Return 204 without exposing customer information
        return make_response("", 204)

    # Return 404 if customer does not exist
    return make_response({"error": "Customer not found"}, 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)


