#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    # search the contracts list for a matching id
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract is None:
        # no matching contract found
        return make_response('', 404)

    # found it - return the contract info with a 200
    return make_response(contract["contract_information"], 200)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        # customer exists, but data is sensitive - confirm existence only, no body
        return make_response('', 204)
    else:
        # customer not found
        return make_response('', 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    