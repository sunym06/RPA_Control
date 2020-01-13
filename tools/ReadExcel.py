import xlrd


class ReadExcel(object):
    _file = r'../data/data.xlsx'
    data = xlrd.open_workbook(_file,'r')

    def get_sheet(self, sheet_name):
        table = self.data.sheet_by_name(sheet_name)
        print(table.nrows)
        return table

    def get_parameter(self, sheet_name):
        table = self.data.sheet_by_name(sheet_name)
        title = ", ".join(table.row_values(0))
        li = []
        for i in range(1, table.nrows):
            li.append(tuple(table.row_values(rowx=i)))
        # r = (title, li)
        return title, li


if __name__ == "__main__":
    a = ReadExcel()
    # # print(a.get_sheet('robot'))
    b = a.get_parameter('robot')
    print(b)
    # _file = r'../data/data.xlsx'
    # data = xlrd.open_workbook(_file, 'r')
    # table = data.sheet_by_name('robot')
    # a = table.row_values(0)
    # print(a)
    # print(type(a))
    # b = ",".join(a)    # print(b)


('robot_name, robot_kind, robot_description, title, key, result, status', [
    ('20200113-102d', '人工参与', '描述：20200113-001', '新增', '32', '操作成功!', '未注册'),
    ('20200113-101d', '人工参与', '描述：20200113-001', '新增', '32', '操作成功!', '未注册'),
    ('20200113-102d', '无人值守', '描述：20200113-001', '新增', '32', '操作成功!', '未注册')])
