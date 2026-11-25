# Flask Contracts Management API

## Project Description

This project is a Flask application that manages contractor and customer information through HTTP routes. It demonstrates how to handle successful requests, missing resources, and sensitive customer information.

## Features

- Retrieve contract information using a contract ID.
- Return HTTP 200 when a contract is found.
- Return HTTP 404 when a contract is not found.
- Verify customer existence without revealing personal information.
- Return HTTP 204 when a customer exists.
- Return HTTP 404 when a customer does not exist.
- Homepage welcome message.

## Routes

| HTTP Method | Endpoint | Response |
|---|---|---|
| GET | `/` | 200 OK |
| GET | `/contract/<id>` | 200 or 404 |
| GET | `/customer/<customer_name>` | 204 or 404 |

## Technologies

- Python
- Flask
- Pytest
- Git and GitHub

## Installation

```bash
git clone YOUR_FORK_URL
cd python-flask-contracts-lab
python3 -m venv venv
source venv/bin/activate
pip install flask pytest
```

## Running the Application

```bash
python server/app.py
```

Open `http://127.0.0.1:5555` in your browser.

## Running Tests

```bash
python -m pytest -v
```

## Example Requests

```bash
curl -i http://127.0.0.1:5555/contract/1
curl -i http://127.0.0.1:5555/contract/100
curl -i http://127.0.0.1:5555/customer/bob
curl -i http://127.0.0.1:5555/customer/mario
```

## Author

Salma Elyas

