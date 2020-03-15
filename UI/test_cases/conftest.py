import time

import pytest

from UI.pages.robots import Robots


@pytest.fixture(scope='function')
def uuid():
    s = str(time.time())
    yield s[6:10]


# @pytest.fixture(scope='function')
# def add_robot(name, description, uuid, op):
#     a = Robots()
#     a.add(name + uuid, description + uuid, op)


@pytest.fixture(scope='function')
def add_robot(name, uuid):
    a = Robots()
    a.add(name + uuid, 'descr iption: add a robot for test!!!, No.' + uuid)


@pytest.fixture(scope='function')
def add_robot_group(name, uuid):
    a = Robots()
    a.add(name + uuid, 'descrip tion: add a robot_group for test!!!, No.' + uuid, '机器人组')


# @pytest.fixture(scope='function')
# def for_bounding(name, description, uuid, add_robot):
#     a = Robots()
#     a.add('group_' + name + uuid, description + uuid, '机器人组')


@pytest.fixture(scope='function')
def unbounded(name, uuid, add_robot, add_robot_group):
    a = Robots()
    a.bounding(name + uuid, [name + uuid])

