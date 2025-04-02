import requests

# Replace with your actual token
DISCOGS_TOKEN = "VmsxZpniRmIKRsibYNMaFJEpmsYhFXodtnxRVipA"

# Define your search query
params = {
    "q": "The Whispers",
    "type": "artist",
    "token": DISCOGS_TOKEN
}

response = requests.get("https://api.discogs.com/database/search", params=params)

# Pretty print the JSON response
if response.status_code == 200:
    data = response.json()
    for result in data.get('results', []):
        print(f"Name: {result.get('title')}, Type: {result.get('type')}")
else:
    print("Error:", response.status_code, response.text)