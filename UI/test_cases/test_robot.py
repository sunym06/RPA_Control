# import time
#
# import pytest
#
# from UI.pages.home import Home
# from UI.pages.robots import Robots
#
#
# class TestRobot(object):
#     a = Home().to_robot()
#
#     @pytest.mark.parametrize(' robot_name, robot_kind, description', [
#         ('auto', '无人值守', 'description'),
#         ('auto', '人工参与', 'description'),
#         ('auto', '人工参与', 'description'),
#         ('auto', '人工参与', 'description')
#
#     ])
#     def test_add_robot(self, robot_name, robot_kind, description, uuid):
#         k, r = self.a.add_robot(robot_name + uuid, robot_kind, description + uuid)
#         assert len(k) > 10
#         assert r == '操作成功!'
#
#     @pytest.mark.parametrize('robot_name, robot_kind, description', [
#         ('for_edit', '人工参与', 'edit again by Python 3.5'),
#         ('for_edit', '无人值守', 'edit again by Python 3.5'),
#         ('for_edit', '人工参与', 'edit again by Python 3.5'),
#         ('for_edit', '无人值守', 'edit again by Python 3.5'),
#         ('for_edit', '无人值守', 'edit again by Python 3.5')
#
#     ])
#     def test_edit_robot(self, robot_name,  robot_kind, description, uuid):
#         self.a.add_robot(robot_name + uuid, robot_kind, description + uuid)
#         k, r = self.a.edit_robot(robot_name + uuid,  '_edited_' + robot_name + uuid, robot_kind, description + '_edit_' + uuid)
#         assert '成功' in r
#
#     @pytest.mark.parametrize('robot_name, robot_kind, description', [
#         ('for_del', '无人值守', 'add robot for del'),
#         ('for_del', '人工参与', 'add robot for del'),
#         ('for_del', '无人值守', 'add robot for del')
#     ])
#     def test_del_robot(self, robot_name,  robot_kind, description, uuid):
#         self.a.add_robot(robot_name + uuid, robot_kind, description + uuid)
#         r = self.a.del_robot(robot_name + uuid)
#         assert '成功' in r
#
#
#     @pytest.mark.parametrize('robot_name', [
#         'auto_edit65895', 'auto_edit65900'
#     ])
#     # todo 考虑到用例独立，需提前绑定用例
#     def test_unbound_robot(self, robot_name):
#         r = self.a.unbound_robot(robot_name)