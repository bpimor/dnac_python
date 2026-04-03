import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
# Cat C ULR + URL for the API call
from DNAC_CONNECTION import BASE_URL, ASSIGNED_DEVICES_UNASSIGNED
# Import Token
from GET_DNAC_TOKEN import headers
# Get the list of sites IDs and names
from DNAC_SITE_TOPOLOGY import sites
# Get the list of unassigned devices IPs
from DNAC_DEVICES_SITE_UNASSIGNED import ip

# Function Payload need for the API call with the IP of the device to assign to a site
def payload_ip(payload):
     payload_data = {
        "device": [
            {
                "ip": str(payload)
            }
        ]
    }
     return payload_data     

# Function to assign a device to a site with its IP address and the site ID selected
def assign_device_to_site(site_id, header, payload): 
    header['__runsync'] = 'false'
    header['__timeout'] = '10'
    header['__persistbapioutput'] = 'true'
    response = requests.post(BASE_URL + ASSIGNED_DEVICES_UNASSIGNED.format(siteId = site_id), headers = header, json = payload, verify=False)
    response_json = response.json()

    if response.status_code == 202:
            # Try different common paths for the Task ID
            task_id = response_json.get('response', {}).get('taskId') or \
                    response_json.get('taskId') or \
                    response_json.get('response') # Sometimes 'response' is the ID string itself
            
            print(f"Assignment request accepted. Task ID: {task_id}")
    else:
        print(f"Error {response.status_code}: {response.text}")




# Print the list of site to select which one we want
print(sites)
# Ask to enter the site number to select
print("Enter site number:")
site_number = int(input())
# Get the site ID from the list of sites based on the user selection
id = sites[site_number]

# For each unassigned device IP, call the function to assign it to the site selected with the payload function to format the data for the API call
for device_ip in ip:
    #  payload_ip(device_ip)
    #  print(payload_ip(device_ip))
     assign_device_to_site(id, headers, payload_ip(device_ip))

