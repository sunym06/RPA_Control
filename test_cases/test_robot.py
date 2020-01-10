import pytest

from data.GetDatas import GetDatas
from pages.MainPage import MainPage


class TestRobot(object):
    file = r'../data/data.xlsx'
    data = GetDatas(file).get_value('robot')

    @classmethod
    def setup_class(cls):
        cls.Pages = MainPage().to_login().login('admin', '111111')
        # print(cls.data)

    # def teardown_method(self):
    #     self.Pages.to_home()

    @pytest.mark.parametrize('robot_name, robot_kind, robot_description, title, key, result, status', data)
    def test_add_robot(self, robot_name, robot_kind, robot_description, title, key, result, status):
        _title, _key, _result, _status = self.Pages.to_robot().add_rob().add_robot(robot_name, robot_kind, robot_description)
        # assert _result == result
        # assert len(_key) == int(key)
        # assert _title == title
        # assert _status == status

    def test_t(self):
        self.Pages.to_robot().add_rob().add_robot('name12', '无人值守', '描述123')
        # self.Pages.to_robot().add_robot().add_robot('name1', '无人值守', '描述123')
