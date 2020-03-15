import logging

import pytest
import requests

from wechart.keys import Keys


@pytest.fixture(scope='session')
def token():
    url = r'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token2 = Keys.get_token()
    # params = {'corpid': 'ww05edb9ead3c6c478',
    #           'corpsecret': 'YQtgwqEpV31UAQwUpv7UQXSrwmL6qT4TyoHSmiCYCSg'
    #           }
    # r = requests.get(url, params=params,
    #                  proxies={'https':'http://127.0.0.1:7788'},
    #                  verify=False).json()
    # print(token)
    return token2


@pytest.fixture(scope='session')
def names():
    return 'tom'


if __name__ == '__main__':
    print(token())