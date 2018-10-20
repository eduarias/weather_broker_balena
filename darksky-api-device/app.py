import time

import requests
from sense_hat import SenseHat

hat = SenseHat()


def collect_data(device_name):
    response = requests.get('https://api.darksky.net/forecast/a8483764bba6a09c45c5ab2192baa671/41.390205,2.154007')
    if response.ok:
        current_weather_data = response.json()['currently']
        res = {'name': device_name,
               'data': {
                   'temperature': current_weather_data['temperature'],
                   'humidity': current_weather_data['humidity'] * 100,
                   'pressure': current_weather_data['pressure'],
               }}
        return res


if __name__ == '__main__':
    name = 'DarkSkyAPI'
    while True:
        r = requests.post('http://cloud_connector:8080/sensor/data',
                          data=collect_data(name))
        time.sleep(60)
