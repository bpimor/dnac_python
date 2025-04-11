# Modules import
import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, DNAC_NETWORK_HEALTH

# Import Token
from GET_DNAC_TOKEN import headers

# DNAC Health connectivity
dnac_network_request = requests.get(BASE_URL + DNAC_NETWORK_HEALTH, headers = headers, verify=False)
dnac_network = dnac_network_request.json()['response'][0]

# Variables for the InfluxDB import
health_score = dnac_network['healthScore']
total_count = dnac_network['totalCount']
bad_count = dnac_network['badCount']
good_count = dnac_network['goodCount']
no_health_count = dnac_network['noHealthCount']
fair_count = dnac_network['fairCount']
maintenance_mode = dnac_network['maintenanceModeCount']
