# In order to run a command there are three API calls required.
# 1. POST 'dna/intent/api/v1/network-device-poller/cli/read-request' providing a list of commands and deviceId, returns a taskId.
# 2. GET 'dna/intent/api/v1/task/{taskId}' poll the task until it completes, providing a fileId.
# 3. GET 'dna/intent/api/v1/file/{fileId}' which returns the results of the commands.

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
text_file = open('sh_env_all.txt', 'w')
for device in devices_list:
    device_hostname = device['hostname']
    device_uuid = device['instanceUuid']
    device_type = device['type'] 
    if "Switch" in device_type or "Router" in device_type:
        print("*****", device_hostname, "*****")
        text_file.writelines(device_hostname)
        # Create the payload with the command to run based on the deviceUuid
        payload = '{ "commands": [ "show environment all" ], "deviceUuids": ["'+device_uuid+'"] }'
        #Send the command to DNAC
        response = requests.post(BASE_URL + DNAC_CLI_COMMAND, headers = headers, verify=False, data = payload)
        # Wait 1 second for the fileId to appear otherwise it shows that the task is in progress
        time.sleep(1)
        # Get the Task_ID
        try: 
            task_id_url = response.json()['response']['url']
        except:
            print("Unreachable")

        # file_Id will be generated via the Task_ID
        file_id_request = requests.get(BASE_URL + task_id_url, headers = headers, verify=False)
        # Remove all unecessaries information to get the file_Id
        file_id = file_id_request.json()['response']['progress']
        file_id = file_id.lstrip('{"fileId:"')
        file_id = file_id.rstrip('"}')

        # Get the results of the command and print
        final_result = requests.get(BASE_URL + URL_ID+file_id, headers = headers, verify=False)
        try:
            print(final_result.json()[0]['commandResponses']['SUCCESS']['show environment all'])
            text_file.writelines(final_result.json()[0]['commandResponses']['SUCCESS']['show environment all'])
        except: 
            print("No data available")