# <<<<<<< HEAD
# from openpyxl import load_workbook
#
#
# class ReadExcel(object):
#
#     _par = r'../data/data.xlsx'
#
#     def __init__(self):
#         self.wk = load_workbook(self._par)
#
#     def get_value(self, sheet_name, row, col):
#         sheet = self.wk[sheet_name]
#         cell = sheet.cell(row, col).value
#         return cell
#
#     def get_row(self, sheet_name, row):
#         rows = []
#         sheet = self.wk[sheet_name]
#         cols = self.wk[sheet_name].max_column
#         for i in range(1, cols):
#             value = sheet.cell(row, i).value
#             if value is None:
#                 value = ''
#             rows.append(value)
#         return rows
#
#     def get_column(self, sheet_name, column):
#         cols = []
#         sheet = self.wk[sheet_name]
#         max_rows = sheet.max_row
#         for i in range(1, max_rows):
#             value = sheet.cell(i, column).value
#             if value is None:
#                 value = ''
#             cols.append(value)
#         return cols
#
#     def get_datas(self, sheet_name):
#         data = []
#         sheet = self.wk[sheet_name]
#         rows = sheet.max_row
#         columns = sheet.max_column
#         for row in range(1, rows + 1):
#             l = []
#             for column in range(1, columns + 1):
#                 col = sheet.cell(row, column).value
#                 l.append(col)
#             data.append(tuple(l))
#         return data
# =======
# import xlrd
#
#
# class ReadExcel(object):
#     _file = r'../data/data.xlsx'
#     data = xlrd.open_workbook(_file,'r')
#
#     def get_sheet(self, sheet_name):
#         table = self.data.sheet_by_name(sheet_name)
#         print(table.nrows)
#         return table
#
#     def get_parameter(self, sheet_name):
#         table = self.data.sheet_by_name(sheet_name)
#         title = ", ".join(table.row_values(0))
#         li = []
#         for i in range(1, table.nrows):
#             li.append(tuple(table.row_values(rowx=i)))
#         # r = (title, li)
#         return title, li
# >>>>>>> origin/master
#
#
# if __name__ == "__main__":
#     a = ReadExcel()
# <<<<<<< HEAD
#     # b = a.get_value('robot', 3, 5)
#     c = a.get_row('robot', 2)
#     d = a.get_datas('robot')
#     f = a.get_column('robot', 3)
#     e = a.wk['robot'].max_row
#     print(c)
#     print(f)
#
# =======
#     # # print(a.get_sheet('robot'))
#     b = a.get_parameter('robot')
#     print(b)
#     # _file = r'../data/data.xlsx'
#     # data = xlrd.open_workbook(_file, 'r')
#     # table = data.sheet_by_name('robot')
#     # a = table.row_values(0)
#     # print(a)
#     # print(type(a))
#     # b = ",".join(a)    # print(b)
#
#
# ('robot_name, robot_kind, robot_description, title, key, result, status', [
#     ('20200113-102d', '人工参与', '描述：20200113-001', '新增', '32', '操作成功!', '未注册'),
#     ('20200113-101d', '人工参与', '描述：20200113-001', '新增', '32', '操作成功!', '未注册'),
#     ('20200113-102d', '无人值守', '描述：20200113-001', '新增', '32', '操作成功!', '未注册')])
# >>>>>>> origin/master
