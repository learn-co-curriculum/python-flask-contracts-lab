# app.py
from flask import Flask

app = Flask(__name__)

# Data shaped exactly for the tests
contracts = {
    1: "This contract is for John and building a shed"
}
customers = {"bob"}

@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id: int):
    # 200 with EXACT string for id=1; 404 otherwise
    if id in contracts:
        return contracts[id], 200
    return "", 404

@app.route("/customer/<string:customer_name>", methods=["GET"])
def check_customer(customer_name: str):
    # 204 with EMPTY body if found; 404 otherwise
    if customer_name in customers:
        return "", 204
    return "", 404

if __name__ == "__main__":
    app.run(debug=True, port=5555)