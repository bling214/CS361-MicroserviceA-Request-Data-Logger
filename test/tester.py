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

if __name__ == "__main__":
    input("Beginning of Test Program.\nPress Enter to continue...\n")

    request_summary()
    input("Database is currently empty.\nPress Enter to continue...\n")

    log_request(log_data_list[0])
    input("Logged first request data.nPress Enter to continue...\n")

    request_summary()
    input("Summary after logging first request data.\nPress Enter to continue...\n")

    log_request(log_data_list[1])
    input("Logged second request data.\nPress Enter to continue...\n")

    request_summary()
    input("Summary after logging second request data.\nEnd of test. Press Enter to finish...")