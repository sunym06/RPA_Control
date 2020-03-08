import json
import logging
import requests
from api.ot.token1 import Token1


class Department(object):
    logging.basicConfig(level=logging.INFO)
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'

    def creat_depart(self):
        data = {
            "name": "开发中心",
            "name_en": "Dev",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        token = Token1().get_token()
        logging.info(token)
        r = requests.post(self.url,
                          params={'access_token': token},
                          json=data,
                          proxies={'https': 'http://127.0.0.1:7788',
                                   'http': 'http://127.0.0.1:7788'
                                   },
                          verify=False
                          ).json()
        logging.info(json.dumps(r, indent=2))


if __name__ == "__main__":
    a = Department()
    a.creat_depart()
