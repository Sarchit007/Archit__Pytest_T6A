import pytest
import requests
# resp = requests.get("https://petstore.swagger.io/v2/store/inventory")
# resp = requests.post("https://petstore.swagger.io/v2/pet")
# print(resp.status_code)
# print(resp.text)
# dic = resp.json()
# print(dic["word"])
# # print(resp.json())
# expected = 200
# actual = resp.status_code
# assert expected == actual ,f"Not Actual {actual} != {expected}"
# print("sucessful")

# payload = {
#   "id": 1,
#   "category": {
#     "id": 1,
#     "name": "string"
#   },
#   "name": "doggie",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 1,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }

# u = "https://petstore.swagger.io/v2/pet/1"
# u = "https://petstore.swagger.io/v2/pet/1"
# response = requests.post(u, json=payload)
# print("new entry")


# res = requests.delete(u)
# print(res.status_code)


# def addPet():
#     u = "https://petstore.swagger.io/v2/pet"
#     payload = {
#         "id": 1,
#         "category": {
#             "id": 1,
#             "name": "string"
#         },
#         "name": "rocky",
#         "photoUrls": [
#             "string"
#         ],
#         "tags": [
#             {
#                 "id": 1,
#                 "name": "string"
#             }
#         ],
#         "status": "available"
#     }
#     res = requests.post(u, json=payload)
#     print(res.status_code)
#     print(res.json()["id"])
#
#
# def checkPet():
#     u = "https://petstore.swagger.io/v2/pet/1"
#     resp = requests.get(u)
#     print(resp.status_code)
#     print("pet is avialable ")
#
# def deletePet():
#     u = "https://petstore.swagger.io/v2/pet/1"
#     rdel = requests.delete(u)
#     print(rdel.status_code)
#     print("pet is deleted")
@pytest.mark.skip
def test_tcheckPet():
    u = "https://petstore.swagger.io/v2/pet/1"
    resp = requests.get(u)
    print(resp.status_code)
    print("pet is avialable ")


@pytest.mark.skipif(True, reason="Condition is False, so test will run")
def test_addPet():
    u = "https://petstore.swagger.io/v2/pet"
    payload = {
        "id": 2,
        "category": {
            "id": 2,
            "name": "string"
        },
        "name": "rocky",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 2,
                "name": "string"
            }
        ],
        "status": "available"
    }
    res = requests.post(u, json=payload)
    assert res.status_code == 200
    assert res.json()["id"] == payload["id"]
    assert res.json()["name"] == "rocky"

# addPet()
# checkPet()
# deletePet()



