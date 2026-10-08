import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://api.sonarcloud.io/organizations/organizations'

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())