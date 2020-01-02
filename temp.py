#!/usr/bin/python

import wmi
import json
import datetime
import requests


def main():

    w = wmi.WMI(namespace="OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    sensor_list = []
    for sensor in temperature_infos:
        json_data = {
                    "time" : str(datetime.datetime.utcnow().isoformat()),
                    "Identifier" : sensor.Identifier,
                    "Name" : sensor.Name,
                    "SensorType" : sensor.SensorType,
                    "Value" : sensor.Value,
                    "Max" : sensor.Max,
                    "Min" : sensor.Min
                }
        json_data = json.dumps(json_data)
        print(json.dumps(json_data, indent=4, sort_keys=True))
        sensor_list.append(json_data)


if __name__ == '__main__':
    main()