import json

import requests

from yapi.base import Base


class Process(Base):
    url = Base.base_url + 'robot/process/'

    def get_process_list(self, page, size=10):
        url = self.url + 'list'
        params = {
            'page': page,
            'size': size
        }
        r = requests.get(url=url, params=params, headers=self.get_headers).json()
        return r

    def add_process(self):
        url = self.base_url + 'robot/process/add'
        data = {
            'processName': '',
            'processCode': '',
            'packageVersionId': '',
            'robotGroupId': '',
            'processDesc': ''
        }
        r = requests.post(url=url, data=data, headers=self.get_headers).json()
        return r


if __name__ == '__main__':
    a = Process()
    # print(json.dumps(a.add_process(1), indent=2))
    print(a.add_process()['message'])