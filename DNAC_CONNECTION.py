# CISCO CATALYST CENTER CREDENTIALS
BASE_URL = 'https://IP'
USERNAME = 'admin' 
PASSWORD = 'PASSWORD' 

# URLs
# TOKEN API
AUTH_URL = '/dna/system/api/v1/auth/token'
# DEVICE COUNT API
DEVICES_COUNT = '/dna/intent/api/v1/network-device/count'
# DEVICE LIST API
DEVICES_LIST = '/dna/intent/api/v1/network-device'
# DEVICE CONFIG API
DEVICE_CONFIGS = '/api/v1/network-device/{networkDeviceId}/config'
# MEMBERSHIP ID
DNAC_MEMBERSHIP_ID = '/api/telemetry-agent/v1/membership/info'
# DEVICES HEALTH
DEVICES_HEALTH = '/dna/intent/api/v1/device-health'
# POE INFO
POE_DETAILS = '/dna/intent/api/v1/network-device/{deviceUuid}/interface/poe-detail'
# DNAC CLI COMMMAND RUNNER
DNAC_CLI_COMMAND = '/dna/intent/api/v1/network-device-poller/cli/read-request'
# DNAC URL FILEID
URL_ID = '/api/v1/file/'
# DNAC INTERFACES
DNAC_INTERFACES_OLD = '/dna/intent/api/v2/networkDevices/{deviceId}/interfaces/query'
DNAC_INTERFACES = '/dna/intent/api/v1/interface/network-device/{deviceId}'
# DNAC INTERFACES COUNT PER DEVICE
DNAC_INT_COUNT = '/dna/intent/api/v1/interface/network-device/{deviceId}/count'
# ISE STATUS
DNAC_ISE_STATUS = '/dna/intent/api/v1/ise-integration-status'
# DNAC VERSION
DNAC_VERSION = '/dna/intent/api/v1/dnac-release'
# DNAC CSSM CONNECTION
DNAC_CSSM_CONNECTION = '/dna/intent/api/v1/connectionModeSetting'
# DNAC EoX
DNAC_EOX = '/dna/intent/api/v1/eox-status/summary'
# DNAC COMPLIANCE
DNAC_COMPLIANCE = '/dna/intent/api/v1/compliance/detail'
# DNAC NETWORK HEALTH GLOBAL
DNAC_NETWORK_HEALTH = '/dna/intent/api/v1/network-health'
# DNAC LICENSE SUMMARY
DNAC_LICENSE_SUMMARY = '/dna/intent/api/v1/licenses/device/summary?order=asc&page_number=1&limit=500'
# DNAC LICENSE STATUS
DNAC_LICENSE_STATUS = '/dna/system/api/v1/license/status'
# DNAC LICENSE USAGE
DNAC_LICENSE_USAGE = '/dna/intent/api/v1/licenses/usage/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}?device_type={device_type}'

#FOLDER_NAME
FOLDER_NAME = 'device_configs'

