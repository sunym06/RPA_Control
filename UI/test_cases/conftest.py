import random
import time

import pytest

from UI.pages.clock import Clock
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
    time.sleep(3)


@pytest.fixture(scope='function')
def add_robot_group(name, uuid):
    a = Robots()
    a.add(name + uuid, 'descrip tion: add a robot_group for test!!!, No.' + uuid, '机器人组')
    time.sleep(3)


@pytest.fixture(scope='function')
def unbounded(name, uuid, add_robot, add_robot_group):
    a = Robots()
    a.bounding(name + uuid, [name + uuid])
    time.sleep(3)


@pytest.fixture(scope='function')
def add_clock(plan_name, task_name, cron_time, uuid):
    a = Clock()
    a.add_clock(plan_name + 'No.' + uuid, task_name, cron_time)
    time.sleep(5)