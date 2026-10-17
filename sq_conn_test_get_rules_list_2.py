import os
import requests
from dotenv import load_dotenv

load_dotenv('../.env')
SQ_KEY = os.getenv('SQ_KEY')

#For API Request Authentication
HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

PARAMS = {
    'organization': 'acor-uk',
    'impactSoftwareQualities':"MAINTAINABILITY",
    'languages':'py'
}

# V1 URL required
V1_URL = 'https://sonarcloud.io/api/'

# V2 URL might also be required
V2_URL = 'https://api.sonarcloud.io/'

SEARCH_METRICS_ENDPOINT = 'metrics/search' # V1
SHOW_SOURCES_ENDPOINT = 'sources/show' #V1
PROVISION_PROJECTS_ENDPOINT = 'alm_integration/provision_projects' #V1
RULES_SEARCH_ENDPOINT = 'rules/search' #V1

SEARCH_ISSUES_ENDPOINT = 'issues/search' #V2
PROJECTS_ENDPOINT = 'projects/projects' #V2
DOP_REPOS_ENDPOINT = 'dop-translation/dop-repositories'#V2

rules_request = requests.get(V1_URL + RULES_SEARCH_ENDPOINT,headers=HEADERS, params=PARAMS)
rules_response = rules_request.json()
print(f'Rules request status code: {rules_request.status_code}')
if rules_request.status_code == 200:
    print(f'Number of rules found: {rules_response.get("total")}')
    rules = rules_response.get('rules', [])
    for rule in rules:
        print(f'{rule.get('key')}')
else:
    print(f'Error: {rules_response.get("errors")}')
    exit(1)