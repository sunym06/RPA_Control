import allure
import pytest

from UI.pages.easypage import Easy


class TestEasy(object):
    a = Easy()

    @allure.title('新增机器人')
    @allure.description('添加各种类的机器人')
    @pytest.mark.parametrize('name, description', [
        ('新增机器人', '新增机器人测试'),
        ('新增机器人', '新增机器人测试')
    ])
    def test_add_robot(self, name, description, uuid):
        key, result = self.a.add('auto_test ' + name + uuid, description + uuid)
        assert len(key) > 10
        assert '成功' in result

    @allure.title('新增机器人组')
    @allure.description('添加各种类的机器人组')
    @pytest.mark.parametrize('name, description', [
        ('新增机器人组', '新增机器人测试组'),
        ('新增机器人组', '新增机器人测试组')
    ])
    def test_add_robot_group(self, name, description, uuid):
        key, result = self.a.add(name + uuid, description + uuid, '机器人组')
        assert '成功' in result

    @allure.title('修改机器人')
    @allure.description('修改机器人测试用例')
    @pytest.mark.parametrize('name, new_name, description, op', [
        ('修改前', '修改后', '修改机器人', '机器人'),
        ('修改前', '修改后', '修改机器人', '机器人'),
    ])
    def test_edit_robot(self, name, new_name, description, uuid, add_robot):
        key, result = self.a.edit(name + uuid, new_name + uuid, description)
        assert '成功' in result

    @allure.title('修改机器人组')
    @allure.description('修改机器人组测试用例')
    @pytest.mark.parametrize('name, new_name, description, op', [
        ('修改前', '修改后', '修改机器人', '机器人组'),
        ('修改前', '修改后', '修改机器人', '机器人组')
    ])
    def test_edit_robot_group(self, name, new_name, description, uuid, add_robot):
        key, result = self.a.edit(name + uuid, new_name + uuid, description, '机器人组')
        assert '成功' in result

    @pytest.mark.parametrize('name, description, op', [
        ('auto_create_for_del',  'for del ', '机器人'),
        ('auto_create_for_del',  'for del ', '机器人')
    ])
    def test_del_robot(self, name, description, op, uuid, add_robot):
        r = self.a.delete(name + uuid)
        assert '成功' in r

    @pytest.mark.parametrize('name, description, op', [
        ('auto_create_for_del', 'for del ', '机器人组'),
        ('auto_create_for_del', 'for del ', '机器人组')

    ])
    def test_del_robot_group(self, name, add_robot, uuid):
        r = self.a.delete(name + uuid, '机器人组')
        assert '成功' in r

    @pytest.mark.parametrize('name,  description, op', [
        ('绑定用机器人', '用来绑定用机器人', '机器人'),
        ('绑定用机器人', '用来绑定用机器人', '机器人')
    ])
    def test_bounding(self, name, uuid, add_robot, for_bounding):
        r = self.a.bounding('group_' + name + uuid, [name + uuid])
        assert '成功' in r

