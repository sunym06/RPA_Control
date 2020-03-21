import pytest

from UI.pages.activ import Activ
from UI.pages.process import Process


class TestProcess(object):
    a = Activ()
    b = Process()

    @pytest.mark.parametrize('name, key, rpa', [
        ('wang12a', 'fe', '1231')
    ])
    def test_upload_process(self, name, key, rpa):
        # self.a.create_act(name, key, rpa)

        self.b.upload_process(name)