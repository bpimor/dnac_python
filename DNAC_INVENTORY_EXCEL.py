# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()

# Create Excel file and write
import xlsxwriter

# Import all variables from DNAC_CONNECTION.py in the same folder as the script
from DNAC_CONNECTION import BASE_URL, USERNAME, PASSWORD, AUTH_URL, DEVICES_LIST

# Import Token
from GET_DNAC_TOKEN import headers


# # Get devices SN by platform ID
# headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
# query_string_params = {'platformId': 'C9115AXI-E'}
# response = requests.get(BASE_URL + DEVICES_LIST, headers = headers, params=query_string_params, verify=False)
# devices = []
# for device in response.json()['response']:
#   devices.append(device['serialNumber'])

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('devices_DNAC.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
# Header creations
worksheet.write(0, 0 , "Platform_ID")
worksheet.write(0, 1 , "SN")
worksheet.write(0, 2 , "Hostname")
worksheet.write(0, 3 , "MAC")
worksheet.write(0, 4 , "Version")
worksheet.write(0, 5 , "MGMT_IP")
worksheet.write(0, 6 , "MGMT_Status")
worksheet.write(0, 7 , "Reachability")

# Row starts at 1 to leave the header row
row = 1

# Get devices information   
response = requests.get(BASE_URL + DEVICES_LIST, headers = headers, verify=False)
devices = []
for device in response.json()['response']:
  worksheet.write(row, 0 , device['platformId'])
  worksheet.write(row, 1 , device['serialNumber'])
  worksheet.write(row, 2 , device['hostname'])
  worksheet.write(row, 3 , device['macAddress'])
  worksheet.write(row, 4 , device['softwareVersion'])
  worksheet.write(row, 5 , device['managementIpAddress'])
  worksheet.write(row, 6 , device['managementState'])
  worksheet.write(row, 7 , device['reachabilityStatus'])
  row += 1

 
# Finally, close the Excel file
# via the close() method.
workbook.close()

