import pytest
import requests


# @pytest.fixture(scope='session')
# def tokens(request):
#     url = r'http://111.231.110.64:8222/api/login'
#     data = {
#         'username': 'admin',
#         'password': '111111'
#     }
#     r = requests.post(url=url, data=data).json()['data']
#     head = {'Authorization': 'Bearer ' + r,
#             'Cookies': 'x-access-token' + r
#             }
#
#     return head

@pytest.fixture(scope='session')
def headers2(a):
    print('a is ' + a)
    yield 'a'
