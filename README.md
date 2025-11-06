# Blake Added

Contract Route Feature
• Added /contract/<id> route to return contract information.
• 200 OK → Contract found, returns JSON with contract details.
• 404 Not Found → Contract ID not found in dataset.

Customer Route Feature

- Added /customers/<name> route to return customers name
- 200 OK Customer found
- 404 Not found - customer name not found

# Lab: Contractors Lab

---

## Overview

Now it is time for you to build your own request responses!

You are working for a company that manages contracts between two parties. You need to manage sensitive data, and as such, you need to build two requests:

- One for **customer information**
- One for **contract information**

You will be using two new response codes:

- **204**: Successful response but no data to send (e.g., confirming a customer exists without sharing data).
- **404**: Not found — we cannot find the requested data.

---

## Tasks

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `GET /contract/<id>`

  - **200**: Contract found — return contract information.
  - **404**: Contract not found.

- `GET /customer/<customer_name>`
  - **204**: Customer found — no information returned (sensitive).
  - **404**: Customer not found.

---

### Task 3: Develop the Code

- Initialize Flask
- Set up routes
- Configure responses

---

### Task 4: Test and Refine

- Debug and test during development using the provided test suite and Flask instance.

---

### Task 5: Document and Maintain

- Commit as you go with meaningful messages.
- Push commit history to GitHub periodically and when the lab is complete.

---

## Tools and Resources

- **GitHub Repo**: _Link to be provided_
- **Flask Quickstart**: [https://flask.palletsprojects.com/en/stable/quickstart/](https://flask.palletsprojects.com/en/stable/quickstart/)

---

## Instructions

### Set Up

Before coding:

1. **Fork and Clone**

   - Go to the provided GitHub repository link.
   - Fork the repository to your GitHub account.
   - Clone the forked repository to your local machine.

2. **Open and Run**
   - Open the project in VSCode.
   - Run `pipenv install` to install dependencies.
   - Run `pipenv shell` to activate the Python shell.

---

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `/contract/<id>`

  - **200**: Contract found — return information
  - **404**: Contract not found

- `/customer/<customer_name>`
  - **204**: Customer found — return no information
  - **404**: Customer not found

---

### Task 3: Develop, Test, and Refine the Code

1. Create a **feature branch**.
2. Build the following routes:

#### `/contract/<id>`

- If the contract ID is found in the given array:
  - Return contract information with a **200** response.
- If not found:
  - Return a **404** response.

#### `/customer/<customer_name>`

- If the customer name is found:
  - Return a **204** response with an empty body.
- If not found:
  - Return a **404** response.

3. Push the feature branch and open a PR on GitHub.
4. Merge into `main`.

---

### Task 4: Document and Maintain

#### Best Practices:

- Add comments to explain logic and purpose.
- Clarify code intent for other developers.
- Include a screenshot of completed work in the README.
- Update the README to reflect functionality using [https://makeareadme.com](https://makeareadme.com).
- Delete stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to exclude sensitive data
