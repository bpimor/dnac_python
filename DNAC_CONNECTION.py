# CISCO DNA CENTER CREDENTIALS
BASE_URL = 'https://dnac_ip_or_fqdn'
USERNAME = 'username'
PASSWORD = 'password'

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

#FOLDER_NAME
FOLDER_NAME = 'device_configs'
