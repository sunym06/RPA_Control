# import pytest
# from UI.pages.home import Home
# from UI.pages.robots import Robots
#
#
# class TestRobotGroup(object):
#     a = Home().to_robot_group()
#
#     @pytest.mark.parametrize('group_name, group_kind, description', [
#         ('auto1_', '开发', 'description'),
#         ('auto2_', '测试', 'description'),
#         ('auto3_', '开发', 'description'),
#         ('auto4_', '测试', 'description'),
#         ('auto5_', '开发', 'description'),
#         ('auto6_', '测试', 'description')
#     ])
#     def test_add_robot_group(self,group_name, group_kind, description, uuid):
#         r = self.a.add_robot_group(group_name + uuid, group_kind, description + uuid)
#         assert r == '操作成功!'
#
#     @pytest.mark.parametrize('group_name,  group_kind, description', [
#         ('for_edit', '开发', 'edit again by Python 3.5'),
#         ('for_edit', '测试', 'edit again by Python 3.5')
#     ])
#     def test_edit_robot_group(self, group_name,  group_kind, description, uuid):
#         self.a.add_robot_group(group_name + uuid, group_kind, description + uuid)
#         r = self.a.edit_robot_group(group_name + uuid, '_edited_' + group_name + uuid, group_kind, description + '_edit_' + uuid)
#         assert '成功' in r
#
#     @pytest.mark.parametrize('group_name,  group_kind, description', [
#         ('for_edit', '开发', 'edit again by Python 3.5'),
#         ('for_edit', '测试', 'edit again by Python 3.5'),
#         ('for_edit', '生产', 'edit again by Python 3.5'),
#     ])
#     def test_del_robot_group(self, group_name,  group_kind, description, uuid):
#         self.a.add_robot_group(group_name + uuid, group_kind, description + uuid)
#         r = self.a.del_robot_group(group_name + uuid)
#         assert '成功' in r
#
#     @pytest.mark.parametrize('robot_name, robot_kind, description, group_name, group_kind, description_group', [
#         ('bound3', '无人值守', 'add for bound', 'group_name3', '测试', 'group_b')
#     ])
#     def test_bound_robot(self, robot_name, robot_kind, description, group_name, group_kind, description_group):
#         Robots().add_robot(robot_name, robot_kind, description)
#         # bounded_list = []
#         self.a.add_robot_group(group_name, group_kind, description_group)
#         self.a.bound_robot_group(group_name, list(robot_name))
