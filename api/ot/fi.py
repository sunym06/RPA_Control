import pytest


def test_fixture(return_data):
    assert  return_data==2
@pytest.fixture()
def return_data():
    return 2