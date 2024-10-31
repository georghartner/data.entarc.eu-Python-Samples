keycloakUrl = "https://iam.entarc.eu/realms/dataentarceu/protocol/openid-connect/token";
clientId = "dataentarceu";
clientSecret = "CciEH31F6xfI2dMhigu0wjqWnrI3bPvz";
username = "?";
password = "?";

import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

data = {
    "grant_type": 'password',
    "client_id": clientId,
    "client_secret":  clientSecret,
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
    print("Request succeeded:", response.json())

    print("Now using access token to request data from API:")

    access_token = response.json()["access_token"]
    url = "https://data-api.entarc.eu/timeseries/test/AT/NAT/AT0020000000000000000000100341061"

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Request succeeded:", response.json())
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)

else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
