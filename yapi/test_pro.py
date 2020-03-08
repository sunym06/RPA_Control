import pytest

from yapi.process import Process


class TestProcess(object):

    def test_get_list(self):
        Process().get_process_list(1)

