import pytest

from tools.GetDatas import GetDatas
from pages.MainPage import MainPage
from tools.ReadExcel import ReadExcel


class TestRobot(object):
    file = r'../data/data.xlsx'
    data = ReadExcel().get_parameter('robot')

    @classmethod
    def setup_class(cls):
        cls.Pages = MainPage().to_login().login('admin', '111111')
        # print(cls.data)

    # def teardown_method(self):
    #     self.Pages.to_home()

    @pytest.mark.parametrize(*data)
    def test_add_robot(self, robot_name, robot_kind, robot_description, title, key, result, status):
        _title, _key, _result, _status = self.Pages.to_robot().add_rob().add_robot(robot_name, robot_kind, robot_description)
        assert _result == result
        assert len(_key) == int(key)
        assert _title == title
        assert _status == status

    @pytest.mark.parametrize('robot_name', ['20200113-112d'])
    def test_del_robot(self, robot_name):
        self.Pages.to_robot().del_rob(robot_name)
