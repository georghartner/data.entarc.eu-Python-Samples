import requests
from urllib.parse import urlencode
import json

keycloakUrl = "https://iam.entarc.eu/realms/dataentarceu/protocol/openid-connect/token";
client_id = "dataentarceu";
client_secret = "CciEH31F6xfI2dMhigu0wjqWnrI3bPvz";
username = "?";
password = "?";
connection_id = "test"
country = "AT"
coding_schema = "NAT"
accounting_point_id = "AT0020000000000000000000100341061"
from_dt = "2024-09-10T00:00:00.000000Z"
to_dt = "2024-010-31T00:00:00.000000Z"
tariffCode = "AWATTAR"

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
    url = f'https://data-api.entarc.eu/timeseries/{connection_id}/{country}/{coding_schema}/{accounting_point_id}/{from_dt}/{to_dt}'
    # url = f'https://data-api.entarc.eu/timeseriesWithPrice/{connection_id}/{country}/{coding_schema}/{accounting_point_id}/{from_dt}/{to_dt}/{tariffCode}'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("Request succeeded:\n", json.dumps(response.json(),indent=2))
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)

else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
