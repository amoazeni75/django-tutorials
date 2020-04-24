import requests


def client():
    credentials = {"username": "admin", "password": "alireza123"}
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login", data=credentials)
    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)
