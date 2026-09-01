from flask import Flask

app = Flask(__name__)


contracts = [
    {
        "id": 1,
        "contractor": "ABC Construction",
        "project": "Office Building",
        "value": 500000
    },
    {
        "id": 2,
        "contractor": "XYZ Contractors",
        "project": "Road Construction",
        "value": 750000
    },
    {
        "id": 3,
        "contractor": "Build Kenya Ltd",
        "project": "Residential Apartments",
        "value": 900000
    }
]


customers = [
    "John Doe",
    "Jane Smith",
    "Mary Wanjiku"
]


@app.route("/")
def home():
    return "Welcome to the Contractor API"


@app.route("/contract/<int:id>")
def get_contract(id):

    contract = next(
        (contract for contract in contracts if contract["id"] == id),
        None
    )

    if contract:
        return contract, 200

    return "Contract not found", 404


@app.route("/customer/<customer_name>")
def get_customer(customer_name):

    if customer_name.lower() in [customer.lower() for customer in customers]:
        return "", 204

    return "Customer not found", 404


if __name__ == "__main__":
    app.run(debug=True, port=5002)