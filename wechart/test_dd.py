import pytest


def demo(a,b):
    return a+b

class TestDD(object):

    def test_demo(self):
        assert int('5') == 5

    @pytest.mark.parametrize('name', ['licy', 'lucy'])
    def test_py(self, name):
        print(name)

    @pytest.mark.parametrize('no1', ['licy', 'lucy'])
    def test_creaat(self, no1):
        a = no1
        print(a)