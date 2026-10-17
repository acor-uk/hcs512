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

# V1 URL required
V1_URL = 'https://sonarcloud.io/api/'

# V2 URL might also be required
V2_URL = 'https://api.sonarcloud.io/'

SEARCH_METRICS_ENDPOINT = 'metrics/search' # V1
SHOW_SOURCES_ENDPOINT = 'sources/show' #V1
PROVISION_PROJECTS_ENDPOINT = 'alm_integration/provision_projects' #V1

SEARCH_ISSUES_ENDPOINT = 'issues/search' #V2
PROJECTS_ENDPOINT = 'projects/projects' #V2
DOP_REPOS_ENDPOINT = 'dop-translation/dop-repositories'#V2

metrics_request = requests.get(V1_URL + SEARCH_METRICS_ENDPOINT,headers=HEADERS)
metrics_response = metrics_request.json()
print(metrics_request.status_code)
print(metrics_response)