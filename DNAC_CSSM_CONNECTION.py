# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_CSSM_CONNECTION

# Import Token
from GET_DNAC_TOKEN import headers

#CSSM Connectivity
cssm_connection_request = requests.get(BASE_URL + DNAC_CSSM_CONNECTION, headers = headers, verify=False)
cssm_connection = cssm_connection_request.json()['response']['connectionMode']
