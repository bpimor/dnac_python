# Modules import
import requests
from requests.auth import HTTPBasicAuth
from tabulate import tabulate

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_MEMBERSHIP_ID

# Import Token
from GET_DNAC_TOKEN import headers

# Get devices information   
response = requests.get(BASE_URL + DNAC_MEMBERSHIP_ID, headers = headers, verify=False)
print("The DNAC Member ID is: *****",response.json()['response']['member_id'], '*****')