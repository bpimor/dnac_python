from INFLUXDB_PUSH import fetch_and_push_devices
from DNAC_DEVICE_COUNT import total_devices, devices_list
from DNAC_VERSION import dnac_version
from DNAC_CSSM_CONNECTION import cssm_connection
from DNAC_NETWORK_HEALTH import health_score, bad_count, good_count, no_health_count, fair_count, maintenance_mode
from DNAC_LICENSES import registration_status, authorization_status, license_usage_device
import time
import datetime


# fetch_and_push_devices(total_devices)
reachability = 0
unreachability = 0

for reachable in range(0,total_devices):
    if devices_list[reachable]["reachabilityStatus"] == "Reachable":
        reachability +=1
    else:
        unreachability +=1


def license_dna_usage(device_type):
    if device_type != 'ise':
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[0], f"Purchased DNA Essential Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[1], f"Purchased DNA Advantage Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[2], f"Used DNA Essential Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[3], f"Used DNA Advantage Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[4], f"Purchased Network Essential Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[5], f"Purchased Network Advantage Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[6], f"Used Network Essential Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[7], f"Used Network Advantage Licenses {device_type}")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[8], "Total Purchased DNA Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[9], "Total Used DNA Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[10], "Total Purchased Network Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[11], "Total Used Network License ")
    else: 
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[0], "Purchased ISE Essential Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[1], "Purchased ISE Advantage Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[2], "Purchased ISE Premier Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[3], "Purchased ISE Virtual Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[4], "Used ISE Essential Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[5], "Used ISE Advantage Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[6], "Used ISE Premier Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[7], "Used ISE Virtual Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[8], "Total Purchased ISE Licenses")
        fetch_and_push_devices("Licenses", license_usage_device(device_type)[9], "Total Used ISE Licenses")
   

# Run the fetch_and_push_devices function every minute
if __name__ == "__main__":
    last_catcenter_push_time = datetime.datetime.now() - datetime.timedelta(days=1)  # Initialize to ensure immediate first push

    while True:
        fetch_and_push_devices("Device", total_devices, "Device Count")
        fetch_and_push_devices("Device", reachability, "Device reachable")
        fetch_and_push_devices("Device", unreachability, "Device unreachable")
        fetch_and_push_devices("Health", health_score, "Health score")
        fetch_and_push_devices("Health", bad_count, "Bad score count")
        fetch_and_push_devices("Health", good_count, "Good score count")
        fetch_and_push_devices("Health", no_health_count, "No score count")
        fetch_and_push_devices("Health", fair_count, "Fair score count")
        fetch_and_push_devices("Health", maintenance_mode, "Maintenance mode count")
        fetch_and_push_devices("Health", good_count, "Good score count")
        license_dna_usage('switch')
        license_dna_usage('router')
        license_dna_usage('wireless')
        license_dna_usage('ise')

        # Check if 24 hours have passed since the last push for Catalyst Center Version
        current_time = datetime.datetime.now()
        if (current_time - last_catcenter_push_time).total_seconds() >= 86400:  # 86400 seconds = 24 hours
            fetch_and_push_devices("CatCenter", dnac_version, "Catalyst Center Version")
            fetch_and_push_devices("CatCenter", cssm_connection, "CSSM Connection Mode")
            fetch_and_push_devices("CatCenter", registration_status, "Smart License registration status")
            fetch_and_push_devices("CatCenter", authorization_status, "Smart License authorization status")

            last_catcenter_push_time = current_time  # Update the last push time

        time.sleep(1800)  # Wait for 30 minutes
