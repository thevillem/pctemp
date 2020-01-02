#!/usr/bin/python

import datetime
import json

import requests
import wmi

# TODO:
# 1. Command line parameter for sending data.
# 2. Changing send_temp to send_msg ?
# 2a. Add timestamp to JSON data before sending.
# 3. Add a logger instead of print for messaging.


def send_temp(stats_list):

    for stat in stats_list:
        requests.post("TBD", json=stat)


def get_temp():
    w = wmi.WMI(namespace="OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    stats_list = []
    for sensor in temperature_infos:
        json_data = {
            "time": str(datetime.datetime.utcnow().isoformat()),
            "Identifier": sensor.Identifier,
            "Name": sensor.Name,
            "SensorType": sensor.SensorType,
            "Value": sensor.Value,
            "Max": sensor.Max,
            "Min": sensor.Min,
        }
        json_data = json.dumps(json_data)
        stats_list.append(json_data)

    return stats_list


def main():

    c = wmi.WMI()
    if c.Win32_Process(name="OpenHardwareMonitor.exe"):
        print("OpenHardwareMonitor is running!")
    else:
        print("OpenHardwareMonitor is not running, exiting.")


if __name__ == "__main__":
    main()
