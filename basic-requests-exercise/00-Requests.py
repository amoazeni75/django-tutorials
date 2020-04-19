# to format the code : Shift+Alt+F

import requests


def main():
    # 200 code example
    response = requests.get("https://www.google.com")
    print("Status Code {}".format(response.status_code))
    print("Headers: ", response.headers)
    print("Content-type: ", response.headers['Content-type'])
    print("Response Text: ", response.text)
    # 404 code example
    response = requests.get("https://www.google.com/alireza-moazeni")
    print("Status Code {}".format(response.status_code))


if __name__ == "__main__":
    main()
