import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Get the environment keys
load_dotenv("../.env")

# Get the SonarQube PAT for API
SQ_KEY = os.getenv("SQ_KEY")

# V1 URL required
V1_URL = "https://sonarcloud.io/api/"

# V2 URL might also be required
V2_URL = "https://api.sonarcloud.io/"

SEARCH_ISSUES_ENDPOINT = "issues/search"
PROJECTS_ENDPOINT = "projects/projects"
SHOW_SOURCES_ENDPOINT = "sources/show"

HEADERS = {
    "Accept": "application/json",
    "Authorization": "Bearer " + SQ_KEY
}

project_params= {
    "organization": "acor-uk",
    "project": "acor-uk_AC_MSc_CS"
}

project_response = requests.get(
    V1_URL + SEARCH_ISSUES_ENDPOINT,
    headers=HEADERS,
    params=project_params
)

print(project_response.status_code)