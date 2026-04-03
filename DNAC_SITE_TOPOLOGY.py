# Modules import
import site

import requests

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, SITE_TOPOLOGY

# Import Token
from GET_DNAC_TOKEN import headers

# Import Token
response = requests.get(BASE_URL + SITE_TOPOLOGY, headers = headers, verify=False)
sites = response.json()['response']['sites']

def site_id (get_sites):
    n = 0
    tab = []
    for site_id in get_sites:
        # print(n, ": " + "Site name: " + site_id['name'] + ", Site ID: " + site_id['id'])
        print(n, ": " + "Site name: " + site_id['name'])
        n+=1
        tab.append(site_id['id'])
    return tab

sites = site_id(sites)