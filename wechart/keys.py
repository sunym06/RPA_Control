import requests


class Keys(object):

    @classmethod
    def get_token(cls):
        url = r'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {'corpid': 'ww05edb9ead3c6c478',
                  'corpsecret': 'YQtgwqEpV31UAQwUpv7UQXSrwmL6qT4TyoHSmiCYCSg'
                  }
        r = requests.get(url, params=params).json()
        tokens = r['access_token']
        return tokens


if __name__ == "__main__":
    a = Keys()
    print(a.get_token())
