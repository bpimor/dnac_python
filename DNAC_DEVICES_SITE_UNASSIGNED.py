# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DEVICE_SITE_UNASSIGNED
from DNAC_DEVICE_COUNT import devices_list

# Import Token
from GET_DNAC_TOKEN import headers

# Import Token
response = requests.get(BASE_URL + DEVICE_SITE_UNASSIGNED, headers = headers, verify=False)
devices_id = response.json()['response']['deviceIds']

# for devices_id in response.json()['response']['deviceIds']:
#     print(devices_id)
n=0
ip = []
for devices in devices_list:
    if devices['id'] in devices_id:
        # print("n:", "Device Name:", devices['hostname'], "Device IP:", devices['managementIpAddress'])
        n+=1
        ip.append(devices['managementIpAddress'])
