import pytest
from wechart.department import Department
from wechart.testcases.read_excel import ExcelRead


class TestDepartment(object):
    file = r'E:\workspaces\RPA_Control\wechart\testcases\test_data.xlsx'
    title, test_data = ExcelRead(file, 'Sheet1').get_data('C2', 'I15')

    @pytest.mark.parametrize(title, test_data)
    def test_create(self, name, name_en, parentid, order, id, errcode, real_id):
        r = Department().create(name=name, name_en=name_en, parentid=parentid, order=order, id=id)
        assert r['errcode'] == 0
        # assert r['id'] == real_id

    @pytest.mark.other
    @pytest.mark.parametrize('name', ['tom', 'lily', 'lucy'])
    def test_name(self, name):
        print(name)

