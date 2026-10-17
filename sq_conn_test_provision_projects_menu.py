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

SEARCH_ISSUES_ENDPOINT = 'issues/search' #V2
PROJECTS_ENDPOINT = 'projects/projects' #V2
DOP_REPOS_ENDPOINT = 'dop-translation/dop-repositories'#V2
SHOW_SOURCES_ENDPOINT = 'sources/show' #V1
PROVISION_PROJECTS_ENDPOINT = 'alm_integration/provision_projects' #V1

def list_repos(url = V2_URL + DOP_REPOS_ENDPOINT, headers = HEADERS):
    repos_params = {
        'organizationId': 'AaEIJhRSTbi2tNkwratl'
    }
    repos_list = []
    repos_response = requests.get(url, headers=headers, params=repos_params)
    repos_json = repos_response.json()
    repos = repos_json.get('repositories')
    count = 0
    for repo in repos:
        if repo.get('private'):
            continue
        if repo.get('importedInCurrentOrg'):
            continue
        count+= 1
        repo_id = repo.get('id')
        repo_name = repo.get('name')
        repo_slug = repo.get('slug')
        repos_list.append((repo_id, repo_name, repo_slug))
        print(f'Project {count} - Name: {repo_name}, ID: {repo_id}, slug: {repo_slug}')
    return repos_list
def select_project():
    pass
#the org name can be easily found from a projects request
org_name = 'acor-uk'

repos = list_repos()
print(repos)
selected_repository = int(input("Select Repo by Index or Enter 0 to Return"))
print(repos[selected_repository - 1])
exit()
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

provision_response = requests.post(V1_URL + PROVISION_PROJECTS_ENDPOINT, headers=headers, params=params)

print(provision_response.status_code)
print(provision_response.json())