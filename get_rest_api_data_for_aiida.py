import requests
from urllib.parse import urlencode
import json

keycloakUrl = "https://iam.entarc.eu/realms/dataentarceu/protocol/openid-connect/token";
client_id = "dataentarceu";
client_secret = "CciEH31F6xfI2dMhigu0wjqWnrI3bPvz";
username = "?";
password = "?";
permission_id = "a3bb84ca-e0e1-4441-a95b-0c4c8c08f3d9"

data = {
    "grant_type": 'password',
    "client_id": client_id,
    "client_secret":  client_secret,
    "username": username,
    "password": password,
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Send the POST request with JSON data
response = requests.post(keycloakUrl, data=urlencode(data), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request succeeded:", json.dumps(response.json(),indent=2))

    print("Now using access token to request data from API:")

    access_token = response.json()["access_token"]
    url = f'https://data-api.entarc.eu/latest_values/{permission_id}'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        obj = json.loads(response.json()[0]["payload"]);

        print("Request succeeded:\n", json.dumps(obj,indent=2))
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)

else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
