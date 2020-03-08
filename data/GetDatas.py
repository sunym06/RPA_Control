import xlrd
import openpyxl


class GetDatas(object):

    def __init__(self, files):
        self.file = files
        self.wb = xlrd.open_workbook(files)

    def get_value(self, sheet_name, start_row=1, end_row=None):
        ws = self.wb.sheet_by_name(sheet_name)
        data = []
        if end_row is None:
            end_row = ws.nrows
        for row in range(start_row - 1, end_row):
            row_tem = tuple(ws.row_values(row))
            data.append(row_tem)
        return data

    def get_range(self, sheet_name, start='A1', end=None):
        #todo 目前仅支持26列之前数据取数
        ws = self.wb.sheet_by_name(sheet_name)
        data = []
        base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        start_row = int(start[1:].upper())
        start_clo = base.index(start[:1].upper()) + 1
        end_row = int(end[1:].upper())
        end_col = base.index(end[:1].upper()) + 1
        title = ws.row_values(start_row - 1, start_colx=start_clo-1, end_colx=end_col)
        for row in range(start_row, end_row):
            cells = tuple(ws.row_values(row, start_colx=start_clo - 1, end_colx=end_col))
            data.append(cells)
        # title.append(data)
        return (title, data)

    def get_datas(self, sheet_name):
        table = self.wb.sheet_by_name(sheet_name)
        title = table.row_values(0)
        d = self.get_value()
        title.append(d)
        return tuple(title)


if __name__ == "__main__":
    file = r'E:\workspaces\RPA_Control\try\Excel_try.xlsx'
    wb = openpyxl.load_workbook(file)
    ws = wb['Sheet1']['A1'].value
    print(ws)

    # a = GetDatas(file)
    # b = xlrd.open_workbook(file)
    # print(b.sheet_by_name('Sheet1').cell(1,2).ctype)
    # ti = a.get_range('Sheet2', start='A1', end='E3')
    # print(ws)
    # print(ti, data)
    # print(a.get_title('Sheet2', 'A1', 'C1'))
    # print(a.get_range('Sheet2', start='b3', end='C4'))
    # print(a.get_value('Sheet2',2,4))
    # wb = xlrd.open_workbook(file)
    # ws = wb.sheet_by_name('Sheet2')
    # # print(ws.row_values(0))
    # # print(ws.cell_type(1,2))
    # print(ws.row_values(8))
    # l = []
    # l.append(tuple(ws.row_values(8)))
    # l.append(tuple(ws.row_values(1)))
    # print(l)


