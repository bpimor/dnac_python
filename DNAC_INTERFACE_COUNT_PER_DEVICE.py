# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_INT_COUNT

# Import Token
from GET_DNAC_TOKEN import headers



def interface_count(deviceid): 
    interface_count = requests.get(BASE_URL + DNAC_INT_COUNT.format(deviceId = deviceid), headers = headers, verify=False)
    return interface_count.json()['response']





