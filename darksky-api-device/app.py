import time
import logging

import requests


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(threadName)-12s %(name)-12s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def collect_data(device_name):
    response = requests.get('https://api.darksky.net/forecast/a8483764bba6a09c45c5ab2192baa671/41.390205,2.154007',
                            params={'units': 'si'})
    if response.ok:
        current_weather_data = response.json()['currently']
        res = {'device_name': device_name,
               'data': {
                   'temperature': current_weather_data['temperature'],
                   'humidity': current_weather_data['humidity'] * 100,
                   'pressure': current_weather_data['pressure'],
               }}
        logging.debug('Data to send: {}'.format(res))
        return res


if __name__ == '__main__':
    name = 'DarkSkyAPI'
    while True:
        r = requests.post('http://cloud_connector:8080/sensor/data',
                          json=collect_data(name)
                          )
        logging.debug('Response: {} - {}'.format(r.status_code, r.text))
        logging.debug('Data sent: {}'.format(r.request.body))
        time.sleep(60)
