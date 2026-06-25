from flask import Flask, jsonify

app = Flask(__name__)

contracts = [
    {"id": 0, "name": "Contract A"},
    {"id": 1, "name": "Contract B"},
    {"id": 2, "name": "Contract C"}
]


customers = [
    {"id": 0, "name": "Customer 1"},
    {"id": 1, "name": "Customer 2"},
    {"id": 2, "name": "Customer 3"}
]

@app.route('/contracts/<int:contract_id>')
def get_contract(contract_id):
    for contract in contracts:
        if contract["id"] == contract_id:
            return jsonify(contract), 200
        
    return jsonify({"error": "Contract not found"}), 404    
pipenv shell
@app.route('/customers/<int:customer_id>')
def get_customer(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return jsonify(customer), 200
        
    return jsonify({"error": "Customer not found"}), 404    

if __name__ == '__main__':
    app.run(debug=True) 