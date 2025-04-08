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
print("Type your show command here: ")
sh_command = input()

#Open the file where the output will be
text_file = open(sh_command + '.txt', 'w')
for device in devices_list:
    device_hostname = device['hostname']
    device_uuid = device['instanceUuid']
    device_type = device['type'] 
    if "Switch" in device_type or "Router" in device_type:
        print("*****", device_hostname, "*****")
        text_file.writelines("***** "+ device_hostname+ " *****\n")
        # Create the payload with the command to run based on the deviceUuid
        payload = '{ "commands": [ "' + sh_command + '" ], "deviceUuids": ["'+device_uuid+'"] }'
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
        try:
            final_result = requests.get(BASE_URL + URL_ID+file_id, headers = headers, verify=False)
        except: 
            print("No data available")
        parsed_result = final_result.json()[0]['commandResponses']['SUCCESS'][sh_command]
        try:
            print(parsed_result)
            text_file.writelines(parsed_result+"\n")
        except: 
            print("No data available")