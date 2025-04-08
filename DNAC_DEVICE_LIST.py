# Modules import
from tabulate import tabulate
# Time is used to wait before printing the results
import time
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_DEVICE_COUNT import devices_list, total_devices

# Import Token
# from GET_DNAC_TOKEN import headers
print(total_devices, "devices currently in the network")

for device in devices_list:
    # print(device)
    # print(device['instanceUuid'])
    device_hostname = device['hostname']
    device_uuid = device['instanceUuid']
    device_id = device['id'] 
    device_ip = device['managementIpAddress']
    device_version = device['softwareVersion']
    print(device_hostname)
    print(device_version)
    print(device_ip)
    print(device['type'])