import requests

# GET api data fetch from URI
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=2&sparkline=false"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful (Status Code 200)
if response.status_code == 200:
    # Convert response to JSON format
    data = response.json()
    print("✅ API Data Fetched Successfully!")
    # Print the JSON response
    print(data)
else:
    print("❌ Failed to fetch data. Status Code:", response.status_code)
