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
for device in devices_list:
    device_hostname = device['hostname']
    device_uuid = device['instanceUuid']
    device_type = device['type'] 
    print("*****", device_hostname, "*****")
    # Create the payload with the command to run based on the deviceUuid
    payload = '{ "commands": [ "show runnin | se CISCO_IDEVID_SUDI" ], "deviceUuids": ["'+device_uuid+'"] }'
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
    parsed_result = final_result.json()[0]['commandResponses']['SUCCESS']['show runnin | se CISCO_IDEVID_SUDI']
    try:
        print(parsed_result)
    except: 
        print("No data available")