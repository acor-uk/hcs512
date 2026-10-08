import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SQ_KEY = os.getenv("SQ_KEY")

url = 'https://sonarcloud.io/api/issues/search'


my_headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + SQ_KEY
}

my_params = {
    'organization': 'acor-uk',
    'project':'acor-uk_AC_MSc_CS'
}

response = requests.get(url, headers=my_headers, params=my_params)

print(response.status_code)
#print(response.json())

issues = response.json().get('issues', [])

for issue in issues:
    startLine = issue.get("textRange").get("startLine")
    endLine = issue.get("textRange").get("endLine")
    startChar = issue.get("textRange").get("startOffset")
    endChar = issue.get("textRange").get("endOffset")
    print(f"Issue found at location ln({startLine}),char({startChar}) to: ln({endLine}), char({endChar})\n")