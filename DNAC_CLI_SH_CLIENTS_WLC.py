# Modules import
import requests
# Time is used to wait before printing the results
import time
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_CLI_COMMAND, URL_ID
from DNAC_DEVICE_COUNT import devices_list
# Import Headers
from GET_DNAC_TOKEN import headers

def number_clients(command_output):
    # Split the output into lines
    lines = command_output.strip().split('\n')
    
    # Initialize variables
    num_clients = 0

    for line in lines:
        if "Number of Clients:" in line:
            num_clients = int(line.split(":")[1].strip())
            return num_clients


def extract_mac_addresses(command_output):
    # Split the output into lines
    lines = command_output.strip().split('\n')
    
    # Initialize variables
    mac_addresses = []
    
    num_clients = number_clients(command_output)
    
    # Check if there are any clients
    if num_clients == 0:
        return mac_addresses  # Return an empty list if no clients are found
    
    # Find the start of the MAC address section
    start_index = lines.index(next(line for line in lines if "MAC Address" in line)) + 2
    
    # Extract MAC addresses
    for i in range(num_clients):
        mac_address_line = lines[start_index + i]
        mac_address = mac_address_line.split()[0]
        mac_addresses.append(mac_address)
    
    return mac_addresses

#Loop for all devices in the list
for device in devices_list:
    device_type = device['family']
    device_hostname = device['hostname']
    device_uuid = device['instanceUuid']
    device_type = device['type'] 

    if "Wireless Controller" in device_type:
        # Create the payload with the command to run based on the deviceUuid
        payload = '{ "commands": [ "show wireless client summary" ], "deviceUuids": ["'+device_uuid+'"] }'
        #Send the command to DNAC
        response = requests.post(BASE_URL + DNAC_CLI_COMMAND, headers = headers, verify=False, data = payload)
        # Wait 1 second for the fileId to appear otherwise it shows that the task is in progress
        time.sleep(10)
        # Get the Task_ID, if it fails, it is probably unreachable
        try: 
            task_id_url = response.json()['response']['url']
        except:
            pass

        # file_Id will be generated via the Task_ID
        sh_wireless_request = requests.get(BASE_URL + task_id_url, headers = headers, verify=False)
        # Remove all unecessaries information to get the file_Id
        file_id = sh_wireless_request.json()['response']['progress']
        file_id = file_id.lstrip('{"fileId:"')
        file_id = file_id.rstrip('"}')

        # Get the results of the command and print
        result = requests.get(BASE_URL + URL_ID+file_id, headers = headers, verify=False)
        # If it fails, it's because there is no data or the interface is not compatible with this command
        try:
            final_result = result.json()[0]['commandResponses']['SUCCESS']['show wireless client summary']
            mac_addresses = extract_mac_addresses(final_result)
            num_clients = number_clients(final_result)
            # print(mac_addresses)
            # print(num_clients)
        except: 
            pass
