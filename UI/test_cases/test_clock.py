import allure
import pytest

from UI.pages.base import Base
from UI.pages.clock import Clock


@allure.feature('定时计划管理部分')
class TestClock(Base):

    a = Clock()

    @allure.title('新增定时计划')
    @allure.description('添加各种类定时计划')
    @pytest.mark.parametrize('plan_name, task_name, cron_time', [
        ('add clock', '打开百度-3', '0/5 * * * * ?'),
        ('add clock', '打开百度-2', '0 0/3 * * * ?'),
        ('add clock', 'www1234', '0 0 17 ? * 2 ')

    ])
    def test_add_clock(self, plan_name, task_name, cron_time, uuid):
        result = self.a.add_clock(plan_name + 'No.:' + uuid, task_name, cron_time)
        assert '成功' in result

    @allure.title('删除定时计划')
    @allure.description('删除各种类定时计划')
    @pytest.mark.parametrize('plan_name, task_name, cron_time', [
        ('auto ', '打开百度-3', '0/5 * * * * ?'),
        ('auto ', '打开百度-2', '0/5 * * * * ?'),
        ('auto ', 'www1234', '0/5 * * * * ?')
    ])
    def test_del_clock(self, plan_name, task_name, cron_time, uuid, add_clock):
        result = self.a.del_process(plan_name + 'No.' + uuid)
        assert '成功' in result

    @allure.title('编辑定时计划')
    @allure.description('编辑各种类定时计划')
    @pytest.mark.parametrize('plan_name, new_name, task_name, cron_time', [
        ('old name', 'add clock', '打开百度-3', '0/5 * * * * ?'),
        ('old name', 'add clock', '打开百度-2', '0 0/3 * * * ?'),
        ('old name', 'add clock', 'www1234', '0 0 17 ? * 2 ')

    ])
    def test_edit_clock(self, plan_name, new_name, task_name, cron_time, uuid, add_clock):
        result = self.a.edit_process(plan_name + 'No.' + uuid, new_name + ' No.' + uuid, task_name, cron_time)
        assert '成功' in result

    @allure.title('切换定时计划状态')
    @allure.description('编辑各种类定时计划')
    @pytest.mark.parametrize('plan_name, task_name, cron_time', [
        ('old name', '打开百度-3', '0/5 * * * * ?'),
        ('old name', '打开百度-2', '0 0/3 * * * ?'),
        ('old name',  'www1234', '0 0 17 ? * 2 ')

    ])
    def test_switch(self, plan_name, task_name, cron_time, uuid, add_clock):
        result = self.a.switch(plan_name + 'No.' + uuid)
        assert '成功' in result

