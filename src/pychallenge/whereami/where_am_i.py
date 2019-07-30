import requests

from pychallenge.whereami.secrets import GOOGLE_API_KEY

API_URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="


def find_me():
    payload = {
        "homeMobileCountryCode": 310,
        "homeMobileNetworkCode": 410,
        "radioType": "gsm",
        "carrier": "Vodafone",
        "considerIp": "true",
        "cellTowers": [],
        "wifiAccessPoints": []
    }

    res = requests.post(API_URL+GOOGLE_API_KEY, json=payload)

    data = res.json()

    return data


if __name__ == "__main__":
    find_me()
