import allure
import pytest

from UI.pages.robots import Robots


@allure.feature('机器人组管理相关功能测试')
class TestRobots(object):
    a = Robots()

    @allure.title('新增机器人')
    @allure.description('添加各种类的机器人')
    @pytest.mark.parametrize('name, description', [
        ('新增机器人', '新增机器人测试'),
        ('新增机器人', '新增机器人测试')
    ])
    def test_add_robot(self, name, description, uuid):
        '''
        :param name: 固定name+ uuid随机字符串
        :param description: 固定name+ uuid随机字符串
        :param uuid:
        :return:
        '''
        allure.step('新增机器人')
        key, result = self.a.add('auto_test ' + name + uuid, description + uuid)
        allure.step('开始断言')
        assert len(key) > 10
        assert '成功' in result

    @allure.title('修改机器人')
    @allure.description('修改机器人测试用例')
    @pytest.mark.parametrize('name, new_name, description', [
        ('修改前', '修改后', 'edit robot'),
        ('修改前', '修改后', 'edit robot'),
    ])
    def test_edit_robot(self, name, new_name, description, uuid, add_robot):
        key, result = self.a.edit(name + uuid, new_name + uuid, description + ', No.'+uuid)
        assert '成功' in result

    @allure.title('删除机器人')
    @allure.description('删除机器人测试用例')
    @pytest.mark.parametrize('name, description', [
        ('auto_create_for_del',  'for del '),
        ('auto_create_for_del',  'for del ')
    ])
    def test_del_robot(self, name, description, uuid, add_robot):
        r = self.a.delete(name + uuid)
        assert '成功' in r

    @allure.title('解绑机器人')
    @allure.description('解绑机器人测试用例')
    @pytest.mark.parametrize('name', [
        ('zhangsan'),
        ('lisi')
    ])
    def test_unbounding(self, name, uuid, unbounded):
        r = self.a.unbounding(name + uuid)

    @allure.title('新增机器人组')
    @allure.description('添加各种类的机器人组')
    @pytest.mark.parametrize('name, description', [
        ('新增机器人组', '新增机器人测试组'),
        ('新增机器人组', '新增机器人测试组')
    ])
    def test_add_robot_group(self, name, description, uuid):
        key, result = self.a.add(name + uuid, description + uuid, '机器人组')
        assert '成功' in result

    @allure.title('修改机器人组')
    @allure.description('修改机器人组测试用例')
    @pytest.mark.parametrize('name, new_name, description, op', [
        ('修改前', '修改后', '修改机器人', '机器人组'),
        ('修改前', '修改后', '修改机器人', '机器人组')
    ])
    def test_edit_robot_group(self, name, new_name, description, op, uuid, add_robot_group):
        key, result = self.a.edit(name + uuid, new_name + uuid, description, op)
        assert '成功' in result

    @allure.title('删除机器人组')
    @allure.description('删除机器人组测试用例')
    @pytest.mark.parametrize('name,  op', [
        ('auto_create_for_del', '机器人组'),
        ('auto_create_for_del', '机器人组')

    ])
    def test_del_robot_group(self, name, op, uuid, add_robot_group):
        r = self.a.delete(name + uuid, '机器人组')
        assert '成功' in r

    @allure.title('绑定机器人')
    @allure.description('绑定机器人测试用例')
    @pytest.mark.parametrize('name', [
        ('绑定用机器人'),
        ('绑定用机器人')
    ])
    def test_bounding(self, name, uuid, add_robot, add_robot_group):
        r = self.a.bounding(name + uuid, [name + uuid])
        assert '成功' in r

    @allure.title('机器人管理搜索')
    @allure.description('机器人管理搜索测试用例')
    @pytest.mark.parametrize('name, kind, status, create_time, create_start, create_end, '
                             'modify_start, modify_end, process, op', [
        ('zhangsan', '无人值守', '空闲', '2020-01-12', None, None,
         '2020-02-20', '2020-03-16', None, "机器人"),
        ('zhangsan', '开发', None, None, '2020-02-20', '2020-03-16',
         None, None, None, '机器人组'),
        ('zhangsan', None, None, None, None, None,
         None, None, 'wang', '机器人日志')
    ])
    def test_search(self, name, kind, status, create_time, create_start, create_end,
                    modify_start, modify_end, process, op):
        num = self.a.search(name, kind, status, create_time, create_start, create_end,
                      modify_start, modify_end, process, op)
        assert num >= 0
