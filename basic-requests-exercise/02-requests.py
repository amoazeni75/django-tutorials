# to format the code : Shift+Alt+F

import requests

# get request without parameters


def main():
    # https://exchangeratesapi.io/ example

    payload = {'base': 'USD', 'symbols': ['USD', 'GBP']}

    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    if response.status_code != 200:
        print("Status Code {}".format(response.status_code))
        raise Exception("An Error Occurred")
    else:
        print("Content-type: ", response.headers['Content-type'])
        data = response.json()
        print('JSON data:', data)


if __name__ == "__main__":
    main()
