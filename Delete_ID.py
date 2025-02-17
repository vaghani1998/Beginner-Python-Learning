import requests

# Delete api ID from URI
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Headers
headers = {"Content-Type": "application/json"}

# Send a DELETE request
response = requests.delete(url)

# Check the response status
if response.status_code == 200 or response.status_code == 204:
    print("✅ Resource deleted successfully!")
else:
    print(f"❌ Failed to delete. Status Code: {response.status_code}")