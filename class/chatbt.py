import requests
API_KEY = 'AIzaSyB5aae-KKw_tCF_eUKyfTAyBB8Fe-pUpCs'

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

parts = []
while(1):
    user_input = input("You: ")
    if user_input == "exit": break
    parts.append({"text": user_input})
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": parts
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    print("status:", response.status_code)
    data = response.json()
    if "candidates" in data:
        print("\nAI:", data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print("Error", data)