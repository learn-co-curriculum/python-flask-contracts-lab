# Flask Contracts Management API

A Flask API for managing contractor relationships between two parties. Implements secure customer data handling with appropriate HTTP status codes.

## Features

- 🔐 **Secure Customer Data** - Returns 204 (No Content) to confirm customer existence without exposing sensitive information
- 📄 **Contract Management** - Retrieves full contract details with proper status codes
- ✅ **RESTful Design** - Uses appropriate HTTP status codes (200, 204, 404)
- 🧪 **Tested Routes** - Verified contract and customer endpoints

## Technologies Used

- **Python 3.12** - Core programming language
- **Flask** - Web framework for API development
- **Pipenv** - Dependency and virtual environment management

## Setup

### Prerequisites
- Python 3.12
- Pipenv

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd python-flask-contracts-lab

# Install dependencies with Pipenv
pipenv install

# Activate virtual environment
pipenv shell

# Navigate to server directory
cd server

# Run the application
python app.py
```

The server will start on `http://127.0.0.1:5555`

## API Endpoints

### Get Contract by ID
```
GET /contract/<id>
```

**Description:** Retrieves contract information by contract ID.

**Parameters:**
- `id` (integer) - Contract ID in URL path

**Responses:**
- `200 OK` - Contract found, returns contract data as JSON
- `404 Not Found` - Contract ID does not exist

**Example:**
```bash
# Valid contract
curl -i http://127.0.0.1:5555/contract/1

# Response: 200 OK
{
  "id": 1,
  "contract_information": "This contract is for John and building a shed"
}

# Invalid contract
curl -i http://127.0.0.1:5555/contract/999
# Response: 404 Not Found
```

---

### Check Customer Exists
```
GET /customer/<customer_name>
```

**Description:** Verifies customer existence without exposing sensitive customer data.

**Parameters:**
- `customer_name` (string) - Customer name in URL path (case-insensitive)

**Responses:**
- `204 No Content` - Customer exists (empty response body for security)
- `404 Not Found` - Customer does not exist

**Example:**
```bash
# Valid customer
curl -i http://127.0.0.1:5555/customer/bob
# Response: 204 No Content (empty body)

# Invalid customer
curl -i http://127.0.0.1:5555/customer/alice
# Response: 404 Not Found
```

**Security Note:** The 204 status code confirms customer existence without returning any personal information, protecting sensitive data.

---

## Sample Data

### Contracts
```python
[
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
```

### Customers
```python
["bob", "bill", "john", "sarah"]
```

## HTTP Status Codes Used

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Contract found and returned successfully |
| 204 | No Content | Customer exists but no data returned (security) |
| 404 | Not Found | Requested resource does not exist |

## Project Structure
```
python-flask-contracts-lab/
├── server/
│   └── app.py              # Flask application with routes
├── Pipfile                 # Python dependencies
├── Pipfile.lock           # Locked dependency versions
├── README.md              # This file
└── screenshot_contracts_api.png  # API demonstration
```

## Testing

### Using curl
```bash
# Test all contract endpoints
curl -i http://127.0.0.1:5555/contract/1
curl -i http://127.0.0.1:5555/contract/2
curl -i http://127.0.0.1:5555/contract/3
curl -i http://127.0.0.1:5555/contract/999  # 404

# Test all customer endpoints
curl -i http://127.0.0.1:5555/customer/bob
curl -i http://127.0.0.1:5555/customer/john
curl -i http://127.0.0.1:5555/customer/alice  # 404
```

### Using Browser

Navigate to:
- `http://127.0.0.1:5555/contract/1`
- `http://127.0.0.1:5555/customer/bob`

## API Screenshot

![API Testing Results](./screenshot_contracts_api.png)

## Development Notes

### Key Implementation Details

**Contract Route:**
- Uses `<int:id>` to ensure ID is parsed as integer
- Searches contracts array for matching ID
- Returns JSON response with `jsonify()` for 200 status
- Returns empty string for 404 status

**Customer Route:**
- Uses `<string:customer_name>` for string parameter
- Case-insensitive matching (converts to lowercase)
- Returns 204 with empty body to protect sensitive data
- Security-first approach: confirms existence without exposing details

**Status Code Implementation:**
```python
# Success with data
return make_response(jsonify(data), 200)

# Success without data (security)
return make_response('', 204)

# Not found
return make_response('', 404)
```

## Future Enhancements

- Add POST/PUT/DELETE operations for full CRUD
- Implement database storage (SQLAlchemy)
- Add authentication/authorization
- Input validation and sanitization
- Error handling middleware
- API versioning
- Rate limiting
- Logging

## Author

**Greg**  
Flatiron School - Flask API Development Lab  
January 2026

## License

Educational project - Flatiron School Curriculum