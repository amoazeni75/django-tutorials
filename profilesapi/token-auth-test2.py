import requests


def client():
    # data = {
    #     "username": "api_user",
    #     "email": "ali@gmail.com",
    #     "password1": "alireza123",
    #     "password2": "alireza123",
    # }
    #
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    token_h = "Token 0c3e4d551992c1cf0c2be9700048960e671cc112"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


client()
