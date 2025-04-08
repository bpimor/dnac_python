# Modules import
import requests
# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
# Create Excel file and write
import xlsxwriter
# Date & Time
import datetime




#import variables to connect to DNAC
from DNAC_CONNECTION import BASE_URL, DEVICES_HEALTH
from GET_DNAC_TOKEN import headers
current_date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print('\n*********** SCRIPT STARTED, ', current_time, ' ***********')
# Name of the files and open the workbook to add the information
workbook = xlsxwriter.Workbook('DEVICES_HEALTH_' + current_date + '.xlsx')
worksheet = workbook.add_worksheet()
#TOKEN CONNECTION

health = requests.get(BASE_URL + DEVICES_HEALTH, headers = headers, verify=False)

# Row starts at 1 to leave the header row
row = 1

#Create the hearders
worksheet.write(0, 0 , "Name")
worksheet.write(0, 1 , "IP")
worksheet.write(0, 2 , "Model")
worksheet.write(0, 3 , "Device Family")
worksheet.write(0, 4 , "MAC")
worksheet.write(0, 5 , "Version")
worksheet.write(0, 6 , "Overall Health")
worksheet.write(0, 7 , "Issue Count")
worksheet.write(0, 8 , "Reachability")

devices = []
for device in health.json()['response']:
  worksheet.write(row, 0 , device['name'])
  worksheet.write(row, 1 , device['ipAddress'])
  worksheet.write(row, 2 , device['model'])
  worksheet.write(row, 3 , device['deviceFamily'])
  worksheet.write(row, 4 , device['macAddress'])
  worksheet.write(row, 5 , device['osVersion'])
  worksheet.write(row, 6 , device['overallHealth'])
  worksheet.write(row, 7 , device['issueCount'])
  worksheet.write(row, 8 , device['reachabilityHealth'])
  row += 1
 
# Finally, close the Excel file
# via the close() method.
workbook.close()


print('\n*********** SCRIPT COMPLETED, ', current_time, ' ***********')