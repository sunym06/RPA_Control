import json
import pytest
import requests
import logging


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = r'https://testerhome.com/api/v3/topics.json?limit=5'

    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(r.json())
        logging.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        r = requests.get(self.url,
                          params={'name': 'tom', 'age': 12},
                          headers={'a': '1', 'b': 'b2'},
                          proxies={'https': '127.0.0.1:7788'},
                          verify=False)
        logging.info(r.url)
        logging.info(r.text)

    def test_http(self, uid):
        url = 'http://localhost/cookies'
        cookies = {'a': 'a1', 'b': uid}
        r1 = requests.get(url, cookies=cookies)
        logging.info(r1.text)

    def test_fixture(self, uid):
        print(uid)
