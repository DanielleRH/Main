# Define imports
import msal
import json
import pandas as pd
import requests
from pprint import pprint
import base64
from github import Github



access_token = "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"
def get_messages(access_token):
    message = ''
    file_name = ''
    for repo in Github(access_token).get_user().get_repos():
        branches = Github(access_token).get_user().get_repo(repo.name).get_branches()
        for b in branches:
            commits = Github(access_token).get_user().get_repo(repo.name).get_commits(b.commit.sha)
            for c in commits:
                message += c.commit.message + ','
                files = c.files
                for f in files:
                    file_name += repo.name +'/' + b.name + '/' + f.filename + ','
    df = pd.DataFrame(message.split(","), columns=['message'])
    df = pd.concat([df, pd.DataFrame(file_name.split(","), columns=['file_name'])], axis=1, join="outer")
    return df.groupby('file_name').head(1).reset_index(drop=True)

print(get_messages(access_token))

