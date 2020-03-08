import json

import requests
url = 'http://124.193.68.233:81/mock/41/robot/edit'
data = {
    'robotId': 'abcd',
    'robotName': 'api_auto',
    'robotType': '0',
    'robotDesc': 'dis'
}
r = requests.post(url=url,
                  data=data,
                  proxies={'http': 'http://127.0.0.1:7788'}
                  )
# print(json.dumps(r.headers, indent=2))
# print(isinstance(r, json))
# r.json()
h:dict = r.json()
print(h)
print(type(h))
for (k,v) in h.items():
    print(k + ':' + v)