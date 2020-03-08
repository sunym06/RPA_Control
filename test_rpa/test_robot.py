import pytest

from test_rpa.Robot import Robot


class TestRobot(object):


    # def test_add_robot(self, data, headers):
    #     r = Robot.add_robot(data=data, headers=headers)
    #     r['code'] == 200
    #     r['message'] == '请求成功'
    #     r['success'] == True

    @pytest.mark.parametrize('Frist',['a', 'b', 'c'])
    @pytest.mark.parametrize('Seond', ['A', 'B'])
    def test_dou(self, Frist, Seond):
        print(Frist + Seond)