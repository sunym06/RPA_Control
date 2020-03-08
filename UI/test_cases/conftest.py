import time

import pytest


@pytest.fixture(scope='function')
def uuid():
    s = str(time.time())
    yield s[5:10]
