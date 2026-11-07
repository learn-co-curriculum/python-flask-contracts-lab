# Contractors Lab API

A small Flask API for looking up contract details and confirming whether a
customer exists. Customer information is treated as sensitive: the customer
endpoint confirms existence without returning customer data.

## Requirements

- Python 3.8
- Pipenv

## Setup and run

Install the project dependencies and start the development server from the
repository root:

```bash
pipenv install
pipenv run flask --app server.app run --port 5555
```

The API is available at `http://127.0.0.1:5555`.

## Endpoints

| Method | Path | Success | Not found |
|---|---|---|---|
| `GET` | `/contract/<id>` | `200` with the contract information | `404` |
| `GET` | `/customer/<customer_name>` | `204` with an empty body | `404` |

Example contract lookup:

```bash
curl -i http://127.0.0.1:5555/contract/1
```

Example customer check:

```bash
curl -i http://127.0.0.1:5555/customer/bob
```

Run the tests with:

```bash
pipenv run pytest
```

## Example response

`GET /contract/1` returns the matching contract information with HTTP `200`:

```text
This contract is for John and building a shed
```
