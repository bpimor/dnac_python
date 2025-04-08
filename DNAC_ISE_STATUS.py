# Modules import
import requests
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_ISE_STATUS
# Import Token
from GET_DNAC_TOKEN import headers


#Device count
ise_status_request = requests.get(BASE_URL + DNAC_ISE_STATUS, headers = headers, verify=False)
# print(ise_status_request.json())

