import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://sonarcloud.io/api/alm_integration/provision_projects'

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}
#the org name can be easily found from a projects request
org_name = 'acor-uk'
#the repo details comes from dop repositories request
repo_id = '1409868459'
repo_name = 'hcs-512'
install_key = f'{org_name}/{repo_name}|{repo_id}'
params = {
    'addAsFavourite':'true',
    'organization': 'acor-uk',
    'installationKeys': install_key,
    'newCodeDefinitionType': 'previous_version',
    'newCodeDefinitionValue': 'previous_version'
}

response = requests.post(url, headers=headers, params=params)

print(response.status_code)
print(response.json())