import requests
from wechart.keys import Keys


class Base(object):
    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/'

    def get_response(self, path, debugs=False, **kwargs):
        kwargs['access_token'] = Keys.get_token()
        if debugs:
            r = requests.get(url=self.base_url + path,
                             params=kwargs,
                             proxies={'https': 'http://127.0.0.1:7788'},
                             verify=False)
        else:
            r = requests.get(url=self.base_url + path,
                             params=kwargs)
        return r

    def post_response(self, path, debugs=False, **kwargs):
        if debugs:
            r = requests.post(self.base_url + path,
                              params={'access_token': Keys.get_token()},
                              json=kwargs,
                              proxies={'https': 'http://127.0.0.1:7788'},
                              verify=False
                              )
        else:
            r = requests.post(self.base_url + path,
                              params={'access_token': Keys.get_token()},
                              json=kwargs
                              )
        return r


if __name__ == '__main__':
    a = Base()
    d = {}
    # result = a.get_response('department/list', de=True, **d).json()
    # print(result)
    d2 = {"id": 1, "name": "新纽_new"}
    result2 = a.post_response('department/update', **d2).json()
    print(result2)

