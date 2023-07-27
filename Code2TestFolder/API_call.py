# Define imports
import msal
import json
import pandas as pd

# Enter the details of your AAD app registration
client_id = '63f06007-3c08-45bf-b4bc-89a77ed2bbdd'
client_secret = 'Ebg8Q~sKW-y5H-0vkVNIKchH_vLnwvyv80z~.ao0'
authority = 'https://login.microsoftonline.com/8zzr5l.onmicrosoft.com'
scope = ['https://graph.microsoft.com/.default']

# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# First, try to lookup an access token in cache
token_result = client.acquire_token_silent(scope, account=None)

# If the token is available in cache, save it to a variable
if token_result:
  access_token = 'Bearer ' + token_result['access_token']
  print('Access token was loaded from cache')

# If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
if not token_result:
  token_result = client.acquire_token_for_client(scopes=scope)
  access_token = 'Bearer ' + token_result['access_token']
  print('New access token was acquired from Azure AD')




# Define imports
import requests

# Copy access_token and specify the MS Graph API endpoint you want to call, e.g. 'https://graph.microsoft.com/v1.0/groups' to get all groups in your organization
url = 'https://graph.microsoft.com/v1.0/sites/8zzr5l.sharepoint.com,9bfe723a-b50f-4169-94a3-9ceba7bf7c94,ad515bd2-4fba-4927-9c7b-08699241b9cd/drive/root/children'
headers = {
  'Authorization': access_token
}

# Make a GET request to the provided url, passing the access token in a header
result = requests.get(url=url, headers=headers).json()


data = result['value']

print(data)

