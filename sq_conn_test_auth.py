import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://api.sonarcloud.io/dop-translation/dop-repositories'

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

params = {
    'organizationId': 'AaEIJhRSTbi2tNkwratl'
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())