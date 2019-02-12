# coding=utf-8
def write_file():
    '''
    编写文件
    '''
    filename='D:/desktop/hello.txt'
    with open(filename,'a') as f:
       #f.write('I LOVE ZMG')
       f.write('I like watching nba games')

if __name__ == '__main__':
    write_file()