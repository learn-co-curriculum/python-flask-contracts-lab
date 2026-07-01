# Flask Contracts API

A simple Flask application that demonstrates dynamic routing and HTTP response codes by managing contract and customer information.

The application provides endpoints for retrieving contract information and verifying whether a customer exists while protecting sensitive customer data.

## Features

* Retrieve contract information using a contract ID.
* Verify whether a customer exists without exposing customer information.
* Uses appropriate HTTP status codes:

  * **200 OK** – Contract found.
  * **204 No Content** – Customer exists, but no data is returned.
  * **404 Not Found** – Requested contract or customer does not exist.

## Project Structure

```text
python-flask-contracts-lab/
├── server/
│   └── app.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── pytest.ini
```

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/python-flask-contracts-lab.git
```

2. Navigate to the project directory.

```bash
cd python-flask-contracts-lab
```

3. Install the project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

## Running the Application

Start the Flask development server:

```bash
flask --app server.app run
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Get Contract Information

**Endpoint**

```text
/contract/<id>
```

**Method**

```text
GET
```

#### Success Response

**Status Code:** `200 OK`

Returns the contract information associated with the specified contract ID.

Example:

```text
This contract is for John and building a shed
```

#### Error Response

**Status Code:** `404 Not Found`

Returned when no contract exists with the specified ID.

---

### Verify Customer

**Endpoint**

```text
/customer/<customer_name>
```

**Method**

```text
GET
```

#### Success Response

**Status Code:** `204 No Content`

Confirms that the customer exists without returning any customer information.

#### Error Response

**Status Code:** `404 Not Found`

Returned when the customer does not exist.

## Example Requests

Retrieve contract information:

```text
GET /contract/1
```

Check if a customer exists:

```text
GET /customer/john
```

Attempt to retrieve a non-existent contract:

```text
GET /contract/10
```

Attempt to verify a non-existent customer:

```text
GET /customer/alice
```

## Technologies Used

* Python 3
* Flask
* Pipenv
* Pytest

## Display Image

Screenshot 2026-07-02 013153.png

## Author

Ruth Juma
