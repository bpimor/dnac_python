from INFLUXDB_PUSH import fetch_and_push_devices
from DNAC_DEVICE_COUNT import total_devices, devices_list
from DNAC_VERSION import dnac_version
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

print(reachability)
print(unreachability)


# Run the fetch_and_push_devices function every minute
if __name__ == "__main__":
    last_catcenter_push_time = datetime.datetime.now() - datetime.timedelta(days=1)  # Initialize to ensure immediate first push

    while True:
        fetch_and_push_devices("Device", total_devices, "Device Count")
        fetch_and_push_devices("Device", reachability, "Device reachable")
        fetch_and_push_devices("Device", unreachability, "Device unreachable")

        # Check if 24 hours have passed since the last push for Catalyst Center Version
        current_time = datetime.datetime.now()
        if (current_time - last_catcenter_push_time).total_seconds() >= 86400:  # 86400 seconds = 24 hours
            fetch_and_push_devices("CatCenter", dnac_version, "Catalyst Center Version")
            last_catcenter_push_time = current_time  # Update the last push time

        time.sleep(1800)  # Wait for 30 minutes