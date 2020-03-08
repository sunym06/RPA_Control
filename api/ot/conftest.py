import time

import pytest


@pytest.fixture(scope='session')
def uid():
    uid = str(time.time()).replace(".", "")[:11]
    return uid
