# Python Flask Contracts Lab

A simple Flask API application that demonstrates route handling and HTTP response codes.

## Features

- Retrieve contract information by ID
- Verify customer existence securely
- Proper use of HTTP response codes:
  - 200 OK
  - 204 No Content
  - 404 Not Found

---

## Installation

Clone the repository:

```bash
git clone <your-github-repo-url>
```

Install dependencies:

```bash
pipenv install
```

Activate virtual environment:

```bash
pipenv shell
```

Run the application:

```bash
python server/app.py
```

---

## Routes

### Home Route

```text
/
```

Returns application status message.

---

### Contract Route

```text
/contract/<id>
```

Example:

```text
/contract/1
```

Responses:

- 200 → Contract found
- 404 → Contract not found

---

### Customer Route

```text
/customer/<customer_name>
```

Example:

```text
/customer/alice
```

Responses:

- 204 → Customer exists
- 404 → Customer not found

---

## Screenshot

![Screenshot(28).png]

---

## Technologies Used

- Python
- Flask
- Pipenv