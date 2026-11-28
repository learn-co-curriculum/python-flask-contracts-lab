# Contractors Lab

## Overview

This Flask application provides read-only routes for contract and customer
lookups. Customer responses intentionally omit sensitive information.

## Routes

| Route | Success response | Not-found response |
| --- | --- | --- |
| `GET /contract/<id>` | `200` with contract information | `404` with an empty body |
| `GET /customer/<customer_name>` | `204` with an empty body | `404` with an empty body |

## Setup

```bash
pipenv install
pipenv run python server/app.py
```

The application runs at `http://localhost:5555`.

## Tests

```bash
pipenv run pytest
```
