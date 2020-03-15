import time

import pytest

from UI.pages.easypage import Easy


@pytest.fixture(scope='function')
def uuid():
    s = str(time.time())
    yield s[5:10]


@pytest.fixture(scope='function')
def add_robot(name, description, uuid, op):
    a = Easy()
    a.add(name + uuid, description + uuid, op)


@pytest.fixture(scope='function')
def for_bounding(name, description, uuid, add_robot):
    a = Easy()
    a.add('group_' + name + uuid, description + uuid, '机器人组')


