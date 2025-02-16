# This test program demonstrates an example of making requests to the Request Data Logger microservice
# by calling the log, summary, and delete REST API endpoints.
import requests

microservice_host='http://127.0.0.1:5000'
log_data_list = [
{
    "time_taken": 5.00,
    "type": "GET"
},
{
    "time_taken": 10.00,
    "type": "GET"
}
]

def request_summary():
    response = requests.get(f'{microservice_host}/summary')
    print(response.json())

def log_request(log_data):
    response = requests.post(f'{microservice_host}/log', json=log_data)
    print(response.json())  # Output: {'status': 'success'}

def clear_all_data():
    response = requests.delete(f'{microservice_host}/delete')
    print(response.json())  # Output: {'status': 'all records deleted'}

if __name__ == "__main__":
    input("Beginning of Test Program.\nPress Enter to request summary...\n")

    request_summary()
    input("Database is currently empty.\nPress Enter to log first data entry...\n")

    print(f"Logging first data: {log_data_list[0]}")
    log_request(log_data_list[0])
    input("Logged first request data.\nPress Enter to fetch summary of request data...\n")

    request_summary()
    input("Summary after logging first request data.\nPress Enter to log second data entry...\n")

    print(f"Logging second data: {log_data_list[0]}")
    log_request(log_data_list[1])
    input("Logged second request data.\nPress Enter to request summary...\n")

    request_summary()
    input("Summary after logging second request data.\nPress Enter clear all data...\n")

    clear_all_data()
    input("Cleared all logging data.\nPress Enter to request summary...\n")

    request_summary()
    input("Summary after logging second request data.\nEnd of test. Press Enter to exit...")
