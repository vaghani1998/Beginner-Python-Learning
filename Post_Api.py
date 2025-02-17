import requests

# Post api data fetch from URI
url = "https://jsonplaceholder.typicode.com/posts"

# Sample Data
data = {
    "title": "My API Test",
    "body": "This is a sample API request using Python.",
    "userId": 1
}

# Headers
headers = {"Content-Type": "application/json"}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Check response
if response.status_code == 201:
    print("✅ Data posted successfully!")
    # Print response data
    print(response.json())
else:
    print("❌ Failed to post data. Status Code:", response.status_code)

