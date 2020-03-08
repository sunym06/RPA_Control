import requests


class Base(object):
    base_url = r'http://111.231.110.64:8222/api/'

    @property
    def get_headers(self):
        data = {
            'username': 'admin',
            'password': '111111'
        }
        r = requests.post(self.base_url + 'login', data=data).json()['data']
        head = {'Authorization': 'Bearer ' + r,
                'Cookies': 'x-access-token' + r
                }
        return head


if __name__ == '__main__':
    a = Base()
    print(a.get_headers)