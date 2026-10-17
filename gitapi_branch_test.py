import os
from github import Github
from github import GithubException
from dotenv import load_dotenv

# Authentication is defined via github.Auth
from github import Auth

load_dotenv("../.env")

GIT_KEY = os.getenv("GIT_KEY")
# using an access token
auth = Auth.Token(GIT_KEY)

# Public Web Github
g = Github(auth=auth)

target_repo = input("Enter a repository to try e.g. myOrg/myrepo: \n")
try:
    repo_request = g.get_repo(target_repo)
    repo_id = repo_request.id
    repo_slug = repo_request.full_name
    repo_privacy = repo_request.private  
    print(repo_request.raw_data)
except GithubException as e:
    print(f'status: {e.status} {e.data.get("message")}')

# To close connections after use
g.close()