# dnac_python
Python scripts that uses the API of the Cisco DNA Center

GET_DNAC_TOKEN.py is used to get the DNAC Token and will be used in other scripts. This should be in the same folder as other scripts.

DNAC_CONNECTION.py gets all the connections details to access the DNAC and all the URLs used for the scripts. This file should also be in the same foleder as the other scripts.

To install the required tools to make the scripts works, you can use the command: pip install -r requirements.txt Requirements.txt is provided in this folder

Needs the following import:
* import requests --> to use the API
* import os --> to access some system information like the file path, etc.
* import datetime --> to be able to print the time
* import urllib3 --> to disable SSL warning in environmnet where devices don't have a valid certificate
* from requests.auth import HTTPBasicAuth --> used for the Authentication of the API
* import xlsxwriter --> to export datas in an Excel file
* from tabulate import tabulate --> to print the datas in a tab
* import influxdb_client --> to push datas in influxdb
