import os
import requests
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


def get_snippet(file_key, issue_from, issue_to):
    source_params = {
        "key": file_key,
        "from": issue_from,
        "to": issue_to
    }

    output_issue_response = requests.get(
        V1_URL + SHOW_SOURCES_ENDPOINT,
        headers=HEADERS,
        params=source_params
    )

    status = output_issue_response.status_code
    snippet = output_issue_response.json()

    #print(status)
    sources = snippet.get("sources",[])
    print(sources[0][1])

project_response = requests.get(
    V1_URL + SEARCH_ISSUES_ENDPOINT,
    headers=HEADERS,
    params=project_params
)

print(project_response.status_code)

issues = project_response.json().get("issues", [])
#print(issues)

for issue in issues:
    start_line = issue.get("textRange").get("startLine")
    end_line = issue.get("textRange").get("endLine")
    start_char = issue.get("textRange").get("startOffset")
    end_char = issue.get("textRange").get("endOffset")
    file_key = issue.get("component")

    print(
        f"Issue found in file: {file_key} at location ln({start_line}), char({start_char}) "
        f"to: ln({end_line}), char({end_char})"
    )

    get_snippet(file_key,start_line,end_line)