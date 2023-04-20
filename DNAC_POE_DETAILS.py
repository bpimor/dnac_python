# Modules import
import requests
import datetime
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
#import variables to connect to DNAC
from DNAC_CONNECTION import BASE_URL, DEVICES_COUNT, DEVICES_LIST, FOLDER_NAME, POE_DETAILS
from GET_DNAC_TOKEN import token


current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n*********** SCRIPT STARTED, ', current_time, ' ***********')

power_draw_total = 0
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

for device in devices_list:
    device_hostname = device['hostname']
    device_id = device['id'] 
    if 'Switch' in device['type']:
      config_str = requests.get(BASE_URL + POE_DETAILS.format(deviceUuid = device_id), headers = headers, verify=False) 
      response = config_str.json()['response']
      print('\n', '\n', device_hostname, "\n")
      for device in config_str.json()['response']: 
        print(device['interfaceName'], ":")
        if device['operStatus'] == 'ON':
            print('PoE',  "\033[1;32;40m ACTIVE \033[0;0m")
        else: 
            print('PoE INNACTIVE')
        if device['adminStatus'] == 'STATIC':
            print('Mode:', "\033[1;31;40m", device['adminStatus'], "\033[0;0m")
        else: 
            print('Mode:', device['adminStatus'])
        print('Allocated Power:', device['allocatedPower'])
        print('Max Power:', device['maxPortPower'])
        power_draw_total += int(device['portPowerDrawn'])
        print('Power Draw', device['portPowerDrawn'], '\n')
        
print('Total power draw:', power_draw_total, "W")
current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('\n*********** SCRIPT COMPLETED, ', current_time, ' ***********')

