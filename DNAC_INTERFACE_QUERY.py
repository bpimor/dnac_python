# File dependencies: DNAC_CONNECTION.py, DNAC_DEVICE_COUNT.py, GET_DNAC_TOKEN.py, DNACL_CLI_SH_TRANSCEIVER.py

# Modules import
import requests
from datetime import datetime 
start_time = datetime.now()
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_INTERFACES
from DNAC_DEVICE_COUNT import devices_list
from GET_DNAC_TOKEN import headers
from DNAC_CLI_SH_TRANCEIVER import *




print("****** SCRIPT BEGINS ******")
#Open the file where the output will be
text_file = open('interfaces_up.txt', 'w')
def is_a_switch (devicetype, deviceuuid, deviceid,): 
    if "Switch" in devicetype:
        text_file.writelines("\n\n***** " + device_hostname + " *****\n")
        response = requests.post(BASE_URL + DNAC_INTERFACES.format(deviceId = deviceid), headers = headers, verify=False)
        # Get the total count of interfaces on the switch for creating a range
        interface_count = response.json()['totalCount']
        # Goes through all the interfaces of the switch
        for interfaces in range(interface_count):
            interface_status = response.json()['response'][interfaces]['values']['adminStatus']
            interface_name = response.json()['response'][interfaces]['values']['name']
            interface_type = response.json()['response'][interfaces]['values']['interfaceType']
            # If the interface is a Physical ethernet and it is UP, then we add the line of the interface and its status
            if interface_status == "UP" and interface_type == "Physical" and "App" not in interface_name and ('Ethernet' in interface_name or 'GigE' in interface_name): 
                text_file.writelines(interface_name + " is " + interface_status + "\n")
                # Then we use the function that will do a sh transceiver detail on these interfaces (function from the DNAC_CLI_SH_TRANSCEIVER.py file)
                cli_sh_transceiver(deviceuuid, interface_name)  

#Loop for all devices in the list
for device in devices_list:
    device_type = device['type'] 
    device_id = device['id']
    device_uuid = device['instanceUuid']
    # Launch the function with the needed variables
    is_a_switch(device_type, device_uuid, device_id)

time_elapsed = datetime.now() - start_time 
text_file.writelines('****** SCRIPT DONE ******\nTime elapsed (hh:mm:ss.ms" {}'.format(time_elapsed))
print('****** SCRIPT DONE ******\nTime elapsed (hh:mm:ss.ms" {}'.format(time_elapsed))