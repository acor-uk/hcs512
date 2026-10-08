import os
from github import Github
from dotenv import load_dotenv

# Authentication is defined via github.Auth
from github import Auth

load_dotenv("../.env")

GIT_KEY = os.getenv("GIT_KEY")
# using an access token
auth = Auth.Token(GIT_KEY)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Get the repository you want to access
repo = g.get_repo("PyGithub/PyGithub")
# Then get the contents of a folder if required, otherwise leave as empty string to get the root folder contents
contents = repo.get_contents("scripts")
#loop through with a simple for
for content_file in contents:
    print(content_file)
    
# To close connections after use
g.close()