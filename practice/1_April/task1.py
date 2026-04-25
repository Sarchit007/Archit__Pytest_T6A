import requests
def addPet():
    u = "https://petstore.swagger.io/v2/pet"
    payload = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "string"
        },
        "name": "rocky",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"
    }
    res = requests.post(u, json=payload)
    print(res.status_code)
    print(res.json()["id"])


def checkPet():
    u = "https://petstore.swagger.io/v2/pet/1"
    resp = requests.get(u)
    print(resp.status_code)
    print("pet is avialable ")

def deletePet():
    u = "https://petstore.swagger.io/v2/pet/1"
    rdel = requests.delete(u)
    print(rdel.status_code)
    print("pet is deleted")