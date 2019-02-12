# coding = utf-8
import xlwt

def set_style(font_name,height,bold=False):
    style = xlwt.XFStyle() #初始化样式

    font = xlwt.Font() #字体
    font.name = font_name
    font.bold = bold
    font.colour_index = 4
    font.height  = height

    style.font = font
    return style

def write_excel(path):
    #创建工作薄
    f = xlwt.Workbook()
    '''
    创建第一个sheet
    '''
    sheet1 =  f.add_sheet("sheet1",cell_overwrite_ok=True)
    row0 =['业务','状态','北京','上海','广州','深圳','状态小计','合计']
    col0 = ['机票','船票','火车票','汽车票','其他']
    status =['预定','出票','退票','业务小计']

    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    
    #生成第一列和最后一列(合并4行)
    #write_merge(x, x + m, y, w + n, string, sytle)
    # x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。
    # 其中，x，y，w，h，都是以0开始计算的。
    i,j = 1,0
    while i<4*len(col0) and j<len(col0):
        sheet1.write_merge(i,i+3,0,0,col0[j],set_style('Arial',220,True)) #第一列
        sheet1.write_merge(i,i+3,7,7) #最后一列'合计'
        i+=4
        j+=1
    sheet1.write_merge(21,21,0,1,'合计',set_style('Times New Roman',220,True))
     #生成第二列
    i = 0
    while i < 4*len(col0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4
    
    '''
    创建第二个sheet
    '''
    sheet2 = f.add_sheet('sheet2',cell_overwrite_ok=True)
    row1 = ['姓名','年龄','出生日期','爱好','关系']
    col1 = ['小杰','小胖','小明','大神']
    #生成第一行
    for i in range(0,len(row1)):
        sheet2.write(0,i,row1[i],set_style('Times New Roman',220,True))
    #生成第一列
    for i in range(0,len(col1)):
        sheet2.write(i+1,0,col1[i],set_style('Times New Roman',220))
    sheet2.write(1,2,'1991/11/11')
    #合并列单元格
    #sheet2.write_merge(3,5,3,2,'暂无')
    #合并行单元格
    sheet2.write_merge(1,2,4,4,'好朋友') 
    #保存文件
    f.save(path)

if __name__ == '__main__':
    write_excel('D:\desktop\地域限额0808.xls')