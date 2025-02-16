import requests

microservice_host='http://127.0.0.1:5000'
log_data = {
    "time_taken": 16.23,
    "type": "GET"
}
response = requests.post(f'{microservice_host}/log', json=log_data)
print(response.json())  # Output: {'status': 'success'}