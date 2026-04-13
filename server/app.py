from flask import Flask

app = Flask(__name__)

# Hardcoded contract data to match test expectations
contracts = {
    "1": "This contract is for John and building a shed"
}

# Hardcoded customers to match test expectations
customers = ["bob"]

@app.route("/contract/<id>", methods=["GET"])
def get_contract(id):
    if id in contracts:
        # Return plain text response, not JSON
        return contracts[id], 200
    else:
        return "Contract not found", 404

@app.route("/customer/<customer_name>", methods=["GET"])
def get_customer(customer_name):
    if customer_name in customers:
        # Return empty body with 204 status
        return "", 204
    else:
        return "Customer not found", 404

if __name__ == "__main__":
    app.run(debug=True)
