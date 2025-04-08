from INFLUXDB_CONNECTION import token, url, org, bucket_cat_center
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# Get the current date and time
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def fetch_and_push_devices(measurement_name, value, field):

    # Initialize the InfluxDB devices
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)



   # Push the data to InfluxDB
    push_to_influxdb(measurement_name, value, write_api, field)


def push_to_influxdb(measurement_name, value, write_api, field):
    # Create a data point with the image metadata
    point = (
        Point(measurement_name)
        # .tag("date", date)
        .field(field, value)
    )

    # Write the point to InfluxDB
    write_api.write(bucket=bucket_cat_center, org=org, record=point)
    print(f"{date}: Pushed {value} to InfluxDB")


