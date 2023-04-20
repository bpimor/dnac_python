import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()
from DNAC_CONNECTION import BASE_URL, USERNAME, PASSWORD, AUTH_URL

'''Finally, the request is done using POST, which returns a json body with the token. The verify=False parameter is used 
in order to query a server with a self-signed certificate. On a production environment, with a valid certificate generated 
by a trusted certificate authority, it is not needed.'''
response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
token = response.json()['Token']
if str(response) != "<Response [200]>":
    print('CONNECTION ERROR')
    quit()

print("DNAC TOKEN IS: \n**********BEGIN**********\n\n",token, '\n\n**********END**********')