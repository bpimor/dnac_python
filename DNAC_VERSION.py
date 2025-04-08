# Modules import
import requests
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_VERSION
from GET_DNAC_TOKEN import headers

dnac_version_request = requests.get(BASE_URL + DNAC_VERSION, headers = headers, verify=False)
dnac_version = dnac_version_request.json()['response']['displayVersion']
 
print(dnac_version_request.json)