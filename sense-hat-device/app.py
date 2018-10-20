import time
import logging

import requests
from sense_hat import SenseHat


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(threadName)-12s %(name)-12s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

hat = SenseHat()


def collect_data(device_name):
    res = {'device_name': device_name,
           'data': {
               'temperature': hat.get_temperature(),
               'humidity': hat.get_pressure(),
               'pressure': hat.get_pressure(),
           }}
    return res


if __name__ == '__main__':
    name = 'SenseHatDevice'
    while True:
        r = requests.post('http://cloud_connector:8080/sensor/data',
                          data=collect_data(name))
        logging.debug('Response: {} - {}'.format(r.status_code, r.text))
        logging.debug('Data sent: {}'.format(r.request.body))
        time.sleep(10)
