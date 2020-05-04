import time

import requests


if __name__ == '__main__':

    while True:
        requests.get('http://localhost:5000/ping')
        time.sleep(1)
