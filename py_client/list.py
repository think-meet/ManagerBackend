import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username\n")
password = getpass("What is your password\n")

auth_reponse = requests.post(endpoint, json={'username':'admin','password':password})
print(auth_reponse.json())

if auth_reponse.status_code == 200:
    token = auth_reponse.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/products/"

    get_reponse = requests.get(endpoint, headers=headers)
    print(get_reponse.json())