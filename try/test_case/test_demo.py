import pytest

@pytest.fixture()
def NN():
    return 32


def test_n(NN):
    assert NN == 32
