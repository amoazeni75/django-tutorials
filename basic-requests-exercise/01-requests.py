# to format the code : Shift+Alt+F

import requests

# pure get request without parameters


def main():
    # https://exchangeratesapi.io/ example
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        print("Status Code {}".format(response.status_code))
        raise Exception("An Error Occurred")
    else:
        print("Content-type: ", response.headers['Content-type'])
        data = response.json()
        print('JSON data:', data)


if __name__ == "__main__":
    main()
