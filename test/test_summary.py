import requests

microservice_host='http://127.0.0.1:5000'
response = requests.get(f'{microservice_host}/summary')
print(response.json())
