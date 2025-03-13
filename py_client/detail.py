import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/products/"

get_response = requests.post(endpoint)
print(get_response.json())