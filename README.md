# CS361-MicroserviceA-Request-Data-Logger
Microservice A - Request Data Logger (Communication Pipe: REST API)

---

# Microservice A - Logging, Summary, and Delete Endpoints

This microservice logs request data (time taken, type, etc.) and provides summary statistics (average time, total number of requests, etc.). It also includes a DELETE endpoint to clear all records.

## Communication Contract

### Endpoint: `/log`

**Description:** Logs each request's time taken and type.

**Method:** POST

**Request Payload:**
- `time_taken`: The time taken to process the request (float).
- `type`: The type of the request (string, e.g., GET, POST).

**Response:**
- Status: 201 Created
- Payload: 
  ```json
  {
    "status": "success"
  }
  
**Error Handling Response:**
- Status: 400 Bad Request if the input is invalid.
  - Payload:
    ```json
    {
      "error": "Invalid input"
    }
- Status: 500 Internal Server Error if an exception occurs.
  - Payload:
    ```json
    {
      "error": "<error_message>"
    }
**Example Call using Python Code:**
```python
import requests

log_data = {
    "time_taken": 1.23,
    "type": "GET"
}
response = requests.post('http://127.0.0.1:5000/log', json=log_data)
print(response.json())  # Output: {'status': 'success'}
```

---

### Endpoint: `/summary`

**Description:** Retrieves summary statistics of logged requests (including average time and total number of requests).

**Method:** GET

**Request Payload:** None

**Response:**
- Status: 200 OK
- Payload: 
  ```json
  {
    "average_time": <float>,
    "total_requests": <int>
  }

**Error Handling Response:**
- Status: 500 Internal Server Error if an exception occurs.
  - Payload:
    ```json
    {
      "error": "<error_message>"
    }

**Example Call using Python Code:**
```python
import requests

response = requests.get('http://127.0.0.1:5000/summary')
print(response.json())  # Output: {'average_time': 1.23, 'total_requests': 100}
```

---

### Endpoint: `/delete`

**Description:** Deletes all records in the database.

**Method:** DELETE

**Request Payload:** None

**Response:**
- Status: 200 OK
- Payload: 
  ```json
  {
    "status": "all records deleted"
  }

**Error Handling Response:**
- Status: 500 Internal Server Error if an exception occurs.
  - Payload:
    ```json
    {
      "error": "<error_message>"
    }

**Example Call using Python Code:**
```python
import requests

response = requests.delete('http://127.0.0.1:5000/delete')
print(response.json())  # Output: {'status': 'all records deleted'}
```
---

## UML Sequence Diagram
![UML Sequence Diagram](images/UML%20for%20CS361%20MicrsoservieA-Request%20Data%20Logger.jpeg)

---

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installing pip

`pip` is the package installer for Python. It is used to install and manage software packages written in Python. Most Python distributions come with `pip` pre-installed. If you need to install it, follow these steps:
- [Official pip Installation Guide](https://pip.pypa.io/en/stable/installation/)
- [How to Install pip on Windows (Stack Overflow)](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
-
  ```bash
  # Download get-pip.py
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  
  # Run the script
  python get-pip.py
  ```
### Installing Flask
Flask is a micro web framework for Python. It is used to build the microservice.
- [Official Flask Installation Guide](https://flask.palletsprojects.com/en/stable/installation/)
  ```bash
  pip install Flask
  ```

### Running the Microservice
1. **Clone the repository:**
-
  ```bash
  git clone https://github.com/bling214/CS361-MicroserviceA-Request-Data-Logger.git
  cd CS361-MicroserviceA-Request-Data-Logger
  ```
2. **Run the Flask application:**
-
  ```bash
  python request_data_logger.py
  ```
  **Note:** Flask is configured to use port 5000 by default. The microservice should now be running on http://127.0.0.1:5000.