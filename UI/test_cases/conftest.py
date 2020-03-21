import random
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



def v(end, start=0):
    return random.randint(start, end)

def cron():
    # 0 / 5 * * * * ?
    second = v(59)
    minutes = v(59)
    hours = v(23)
    day = v(31)
    month = v(12)

    for i in range(10):
        s = random.randint(1, 5)
        print(s)

a = cron()