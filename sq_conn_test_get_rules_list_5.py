import os
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from dotenv import load_dotenv

"""
Based upon:

https://sonarcloud.io/api/rules/search?facets=impactSoftwareQualities%2Crepositories%2Cstatuses%2CcomplianceStandards&organization=acor-uk&ps=1&s=name&activation=true&impactSoftwareQualities=MAINTAINABILITY&languages=py&qprofile=AaEIJhyFTbi2tNkwravg 

"""
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
    'languages':'py',
    'qprofile':'AaEIJhyFTbi2tNkwravg',
    'activation':'true',
    'statuses':'READY'
}

# V1 URL required
V1_URL = 'https://sonarcloud.io/api/'

# V2 URL might also be required
V2_URL = 'https://api.sonarcloud.io/'

RULES_SEARCH_ENDPOINT = 'rules/search' #V1

rules_request = requests.get(V1_URL + RULES_SEARCH_ENDPOINT,headers=HEADERS, params=PARAMS)
rules_response = rules_request.json()
print(f'Rules request status code: {rules_request.status_code}')
if rules_request.status_code == 200:
    print(f'Number of rules found: {rules_response.get("total")}')
    rules = rules_response.get('rules', [])
    rules_list = []
    for rule in rules:
        key = rule.get('key')
        name = rule.get('name')
        type = rule.get('type')
        description = rule.get('htmlDesc')
        clean_desc = bs(description, "html.parser").get_text(" ", strip=True)
        rules_list.append({
            'key': key,
            'name': name,
            'type': type,
            'description': clean_desc
        })
        print(f'Key: {key}, Name: {name}, Type: {type}')
    try:
        df = pd.DataFrame(rules_list)
        df.to_csv('core_rules_list.csv', index=False)
        print("Rules list saved to core_rules_list.csv")
    except Exception as e:
        print(f"Error saving rules list to CSV: {e}")
else:
    print(f'Error: {rules_response.get("errors")}')
    exit(1)