#!/usr/bin/python3
import requests
url = 'http://158.69.76.135/level0.php?id=127&holdthedoor=Submit'
for i in range(10):
    requests.post(url)
