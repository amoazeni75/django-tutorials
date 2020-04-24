import requests


def client():
    # credentials = {"username": "admin", "password": "alireza123"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    token_h = "Token 2a53b170eab8aa6d8ae9bbd1cb4cf191ec12dbfc"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)
    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


client()
