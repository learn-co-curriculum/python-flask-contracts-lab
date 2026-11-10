Contractors Lab
Overview

This Flask application manages customer and contract requests while protecting sensitive customer information.

Routes
Contract Information

GET /contract/<id>

200: Returns contract information when the contract exists.
404: Returns an error when the contract cannot be found.
Customer Information

GET /customer/<customer_name>

204: Confirms the customer exists without returning personal information.
404: Returns an error when the customer cannot be found.
Technologies
Python
Flask
Installation
Clone the repository.
Install dependencies:

pipenv install

Activate the environment:

pipenv shell

Start Flask from the server directory:

python -m flask --app app run

Testing

The following responses were tested:

/contract/1 — 200
/contract/99 — 404
/customer/John — 204
/customer/Unknown — 404
Security

Customer information is not returned by the customer route. A 204 response confirms existence without exposing personal data.

![alt text](<Screen Shot 2026-11-09 at 10.57.34 PM.png>)