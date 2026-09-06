# Contract Management Flask API

## Description

This project is a Flask application for managing contractor contract and customer requests.

The application demonstrates how different HTTP response status codes can be used to protect sensitive customer information while still confirming whether a resource exists.

## Features

* Contract information lookup
* Customer existence verification
* `200 OK` response for existing contracts
* `404 Not Found` response for unavailable contracts or customers
* `204 No Content` response for existing customers
* Customer information is not exposed because it is sensitive
* Automated testing with pytest

## Routes

### Contract Route

**Endpoint:**

`/contract/<id>`

If the contract ID exists, the application returns the contract information with a `200` response.

Example:

`/contract/1`

Response:

`This contract is for John and building a shed`

If the contract does not exist, the application returns:

`404 Not Found`

### Customer Route

**Endpoint:**

`/customer/<customer_name>`

If the customer exists, the application returns:

* Status: `204 No Content`
* Empty response body

This confirms that the customer exists without exposing sensitive customer information.

If the customer does not exist, the application returns:

`404 Not Found`

## Available Data

### Contracts

The application contains three sample contracts:

* Contract 1 — John and building a shed
* Contract 2 — Deck for a business
* Contract 3 — Ownership of a car

### Customers

The application contains the following customers:

* bob
* bill
* john
* sarah

## Running the Application

Activate the Pipenv environment:

```bash
pipenv shell
```

Start the Flask application:

```bash
python3 server/app.py
```

The application runs on:

`http://127.0.0.1:5555`

## Testing

Run the test suite:

```bash
pytest
```

All six tests pass successfully.

## Technologies Used

* Python
* Flask
* pytest
* Pipenv
* Git
* GitHub

## Project Status

The required contract and customer routes have been implemented, tested, and merged into the `main` branch.
