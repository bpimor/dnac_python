# Modules import
import requests
import os
import datetime

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()

#import variables to connect to DNAC
from DNAC_CONNECTION import BASE_URL, DEVICES_COUNT, DEVICES_LIST, DEVICE_CONFIGS, FOLDER_NAME
from GET_DNAC_TOKEN import token

current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n*********** SCRIPT STARTED, ', current_time, ' ***********')

#Device count
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
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

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

for device in devices_list:
    device_hostname = device['hostname']
    device_id = device['id']    
    filename_path = FOLDER_NAME + '/' + device_hostname + '.txt'
    config_str = requests.get(BASE_URL + DEVICE_CONFIGS.format(networkDeviceId = device_id), headers = headers, verify=False) 
    
    try:

        # not all Cisco DNA Center devices have a configuration file, for example AP's
        # attempting to read the configuraiton file will create an error
        config_str = requests.get(BASE_URL + DEVICE_CONFIGS.format(networkDeviceId = device_id), headers = headers, verify=False) 
    
        # save the configuration file and path defined
        with open(filename_path, 'w') as filehandle:
            filehandle.write('%s\n' % config_str.json()['response'])
            print('Saved configuration file with the name: ', filename_path)
    except:
        pass

current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n*********** SCRIPT COMPLETED, ', current_time, ' ***********')
