# coding = utf-8
'''
    excel文件的读取
'''
import xlrd

def readexcel(path):
    workbook = xlrd.open_workbook(path)
    sheets =  workbook.sheet_names()
    # 打印出来信息
    for sname in sheets:
        print(sname)
    #获取第一个sheet
    worksheet = workbook.sheet_by_name(sheets[0])
    #获取sheet中的行数和列数
    print(worksheet.nrows)
    print(worksheet.ncols)
    #取出其中的cell值
    print(worksheet.cell(0,1).value)
    #使用行列索引
    print(worksheet.row(0)[0].value)
    #获取cell的类型s
    print(worksheet.row(0)[0].ctype)
    #循环遍历第一行
    for cell in worksheet.row(0):
        print(cell.value)
    #循环遍历第一列
    for cell in worksheet.col(0):
        if cell.value is not None and cell.value !='':
            print(cell.value)


if __name__ == '__main__':
    readexcel('D:\desktop\地域限额0807.xlsx')

