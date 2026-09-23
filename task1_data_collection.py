import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {
    "User-Agent": "TrendPulse/1.0"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json()[:10])
