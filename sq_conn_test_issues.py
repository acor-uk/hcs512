#2409808 Oct 2026
import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://sonarcloud.io/api/rules/search'

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

params = {
    'organization': 'acor-uk',
    'activation':'true',
    'languages':'python'
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)

for rule in response.json():
    print(rule)