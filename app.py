from flask import Flask

app = Flask(__name__)

contracts = [
    {"id": 0, "info": "This contract is for John and building a shed"},
    {"id": 1, "info": "This contract is for Alice and painting a house"},
    {"id": 2, "info": "This contract is for Bob and fixing a roof"}
]

customers = ["John", "Alice", "Bob"]


@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["info"], 200
    return "", 404


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return "", 204
    return "", 404


if __name__ == '__main__':
    app.run(debug=True)