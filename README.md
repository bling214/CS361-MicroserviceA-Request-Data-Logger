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
## UML Sequence Diagram
![UML Sequence Diagram](images/UML%20for%20CS361%20MicrsoservieA-Request%20Data%20Logger.jpeg)