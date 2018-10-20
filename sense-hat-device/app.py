import time

import requests
from sense_hat import SenseHat

hat = SenseHat()


def collect_data(device_name):
    res = {'name': device_name,
           'data': {
               'temperature': hat.get_temperature(),
               'humidity': hat.get_pressure(),
               'pressure': hat.get_pressure(),
           }}
    return res


if __name__ == '__main__':
    name = 'SenseHat'
    while True:
        r = requests.post('http://cloud_connector:8080/sensor/data',
                          data=collect_data(name))
        time.sleep(10)