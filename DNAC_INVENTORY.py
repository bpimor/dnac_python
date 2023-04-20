# Modules import
import requests
from tabulate import tabulate


# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DEVICES_LIST

# Import Token
from GET_DNAC_TOKEN import token

# # Get devices SN by platform ID
# headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
# query_string_params = {'platformId': 'C9115AXI-E'}
# response = requests.get(BASE_URL + DEVICES_LIST, headers = headers, params=query_string_params, verify=False)
# devices = []
# for device in response.json()['response']:
#   devices.append(device['serialNumber'])


# # Get devices information   
# headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
# response = requests.get(BASE_URL + DEVICES_LIST, headers = headers, verify=False)
# devices = []
# for device in response.json()['response']:
#   version = device['softwareVersion']
#   sn = device['serialNumber']
#   mac = device['macAddress']
#   hostname = device['hostname']
#   mgmt_state = device['managementState']
#   mgmt_ip = device['managementIpAddress']
#   platform_id = device['platformId']
#   reachability = device['reachabilityStatus']
#   devices = [(platform_id, sn, hostname, mac, version, mgmt_ip, mgmt_state, reachability)]
#   my_headers = ["Platform_ID", "SN", "Hostname", "MAC", "Version", "MGMT_IP", "MGMT_State", "Reachability"]
#   print(tabulate(devices, headers=my_headers, tablefmt="grid"))

# Optimized version
# Get devices information   
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
response = requests.get(BASE_URL + DEVICES_LIST, headers = headers, verify=False)
devices = []
for device in response.json()['response']:
  value = (device['platformId'], device['serialNumber'], device['instanceUuid'], device['hostname'], device['macAddress'], device['softwareVersion'], device['managementIpAddress'], device['managementState'], device['reachabilityStatus'])
  devices.append(value)
my_headers = ["Platform_ID", "SN", "UUID", "Hostname", "MAC", "Version", "MGMT_IP", "MGMT_State", "Reachability"]
# print(tabulate(devices, headers=my_headers, tablefmt="grid"))
table = tabulate(devices, headers=my_headers, tablefmt="grid")
print(table)
