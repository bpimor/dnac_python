# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DEVICES_COUNT, DEVICES_LIST

# Import Token
from GET_DNAC_TOKEN import headers

#Device count
device_count = requests.get(BASE_URL + DEVICES_COUNT, headers = headers, verify=False)
total_devices = device_count.json()['response']
devices_list = []
remaining_device_count = total_devices
device_offset = 1
device_limit = 500

while remaining_device_count > 0:
    device_info = requests.get(BASE_URL + DEVICES_LIST, headers = headers, verify=False)
    devices_list.extend(device_info.json()['response'])
    device_offset += device_limit
    remaining_device_count -= device_limit