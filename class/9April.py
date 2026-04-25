import requests
API_KEY = ''

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key" :  API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    "contents":[
        {
            "parts":[
                {"text":"Explain api testing in simple terms"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print("status:" , response.status_code)
data = response.json()
print(data)

if "candidates" in data:
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("Error",data)