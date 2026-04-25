import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url= "https://www.shoppersstack.com/shopping/"
token = ""
user_id = ""



def add():
    data = {
            "city": "Jaipur",
            "country": "India",
            "email": "transfromerog@gmail.com",
            "firstName": "archit",
            "gender": "MALE",
            "lastName": "saxena",
            "password": "archit",
            "phone": 7895505318,
            "state": "RJ",
            "zoneId": "ALPHA"
            }

    response = requests.post(f"{base_url}/shoppers", json=data,verify=False)
    print(response.status_code)
    print(response.json())


def user_login():
    global user_id
    data = {
            "email": "transfromerog@gmail.com",
            "password": "archit",
            "role" : "SHOPPER"
    }


def test_user_info():
    u_id = 383666
    response = requests.get(f"{base_url}/shoppers/{u_id}", verify=False)
    print(response.status_code)
