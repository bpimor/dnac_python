# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_CLIENT_ASSURANCE
from DNAC_CLI_SH_CLIENTS_WLC import mac_addresses, num_clients

# Import Token
from GET_DNAC_TOKEN import headers


# To manually enter a MAC Address
# print('Enter Client MAC Address:')
# mac_address = input()

# Client Health
def client_health(mac_address):
    dnac_client_health_request = requests.get(BASE_URL + DNAC_CLIENT_ASSURANCE.format(client_mac = mac_address), headers = headers, verify=False).json()['detail']
    return dnac_client_health_request

for mac in range(num_clients):
    snr = client_health(mac_addresses[mac])['snr']
    rssi = client_health(mac_addresses[mac])['rssi']
