# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_LICENSE_SUMMARY, DNAC_LICENSE_STATUS, DNAC_LICENSE_USAGE

# Import Token
from GET_DNAC_TOKEN import headers

# Smart Account license Connectivity
dnac_license_status_request = requests.get(BASE_URL + DNAC_LICENSE_STATUS, headers = headers, verify=False)
dnac_license_summary_request = requests.get(BASE_URL + DNAC_LICENSE_SUMMARY, headers = headers, verify=False)

dnac_license_status = dnac_license_status_request.json()['response']
virtual_account_name = dnac_license_summary_request.json()['response'][0]['virtual_account_name']

# Variables for the InfluxDB import
registration_status = dnac_license_status['registrationStatus']['status']
authorization_status = dnac_license_status['authorizationStatus']['status']
smart_account_id = dnac_license_status['smartAccountId']


# DNAC License Usage
def license_usage_device(device_type): 
    license_usage_request = requests.get(BASE_URL + DNAC_LICENSE_USAGE.format(smart_account_id = smart_account_id, virtual_account_name = virtual_account_name, device_type = device_type), headers = headers, verify=False)
    if device_type != 'ise':
        purchased_dna_essential_count = license_usage_request.json()['purchased_dna_license']['license_count_by_type'][0]['license_count']
        purchased_dna_advantage_count = license_usage_request.json()['purchased_dna_license']['license_count_by_type'][1]['license_count']
        total_purchased_dna_count = license_usage_request.json()['purchased_dna_license']['total_license_count']
        used_dna_essential_count = license_usage_request.json()['used_dna_license']['license_count_by_type'][0]['license_count']
        used_dna_advantage_count = license_usage_request.json()['used_dna_license']['license_count_by_type'][1]['license_count']
        total_used_dna_count = license_usage_request.json()['used_dna_license']['total_license_count']
        purchased_networ_essential_count = license_usage_request.json()['purchased_network_license']['license_count_by_type'][0]['license_count']
        purchased_network_advantage_count = license_usage_request.json()['purchased_network_license']['license_count_by_type'][1]['license_count']
        total_purchased_network_count = license_usage_request.json()['purchased_network_license']['total_license_count']
        used_network_essential_count = license_usage_request.json()['used_network_license']['license_count_by_type'][0]['license_count']
        used_network_advantage_count = license_usage_request.json()['used_network_license']['license_count_by_type'][1]['license_count']
        total_used_network_count = license_usage_request.json()['used_network_license']['total_license_count']
        #return in this order: Purchased DNA Essential, Advantage, then Used DNA Essential, Advantage and Purchased Network Essential, Advantage and Used Network Essential, Advantage and total purchased license DNA, Network and same for total used license DNA, Network.
        return purchased_dna_essential_count, purchased_dna_advantage_count, used_dna_essential_count, used_dna_advantage_count, purchased_networ_essential_count, purchased_network_advantage_count, used_network_essential_count, used_network_advantage_count, total_purchased_dna_count, total_used_dna_count, total_purchased_network_count, total_used_network_count
    else: 
        purchased_ise_essential_count = license_usage_request.json()['purchased_ise_license']['license_count_by_type'][0]['license_count']
        purchased_ise_advantage_count = license_usage_request.json()['purchased_ise_license']['license_count_by_type'][1]['license_count']
        purchased_ise_premier_count = license_usage_request.json()['purchased_ise_license']['license_count_by_type'][2]['license_count']
        purchased_ise_virtual_count = license_usage_request.json()['purchased_ise_license']['license_count_by_type'][3]['license_count']
        total_purchased_ise_count = license_usage_request.json()['purchased_ise_license']['total_license_count']
        used_ise_essential_count = license_usage_request.json()['used_ise_license']['license_count_by_type'][0]['license_count']
        used_ise_advantage_count = license_usage_request.json()['used_ise_license']['license_count_by_type'][1]['license_count']
        used_ise_premier_count = license_usage_request.json()['used_ise_license']['license_count_by_type'][2]['license_count']
        used_ise_virtual_count = license_usage_request.json()['used_ise_license']['license_count_by_type'][3]['license_count']
        total_used_ise_count = license_usage_request.json()['used_ise_license']['total_license_count']
        #return in this order: Purchased ISE Essential, Advantage, Premier, Virtual then Used ISE Essential, Advantage, Premier, Virtual, Total purchased license and Total used license. 
        return purchased_ise_essential_count, purchased_ise_advantage_count, purchased_ise_premier_count, purchased_ise_virtual_count, used_ise_essential_count, used_ise_advantage_count, used_ise_premier_count, used_ise_virtual_count, total_purchased_ise_count, total_used_ise_count


print(license_usage_device('ise'))
print(license_usage_device('switch'))
print(license_usage_device('router'))
print(license_usage_device('wireless'))
