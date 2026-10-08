import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://api.sonarcloud.io/projects/projects'

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

params = {
    'organizationIds': '616bd196-efc5-4225-ba19-7ca88167e4e0'
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())

for project in response.json().get('projects', []):
    print(f"Project Key: {project.get('key')}, Name: {project.get('name')}, Visibility: {project.get('visibility')}")