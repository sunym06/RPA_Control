import logging

import requests


class Token1(object):
    logging.basicConfig(level=logging.INFO)
    token = ''

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url,
                         params={'corpid': 'ww05edb9ead3c6c478',
                                 'corpsecret': 'YQtgwqEpV31UAQwUpv7UQXSrwmL6qT4TyoHSmiCYCSg'
                                 }
                         ).json()
        logging.info(r['access_token'])
        return r['access_token']


if __name__ == '__main__':
    a = Token1()
    a.get_token()
