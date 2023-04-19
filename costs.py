import requests

# Java endpoint URL
url = 'http://example.com/java_endpoint'

# Send GET request to Java endpoint
response = requests.get(url)

# Check als request succesvol is
if response.status_code == 200:
    # Extract data van response
    data = response.json()
    # bewerk de data
    print(data)
else:
    print(f'Request failed with status code {response.status_code}')