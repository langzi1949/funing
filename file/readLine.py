# coding = UTF-8

def main():
    '''
    逐行读取数据
    '''
    with open('D:\\gitlab_workspace\\df-creditPlatform\\src\\main\\java\\com\\namibank\\df\\creditplatform\\fraudmetrix\\dao\\domain\\AuditReport.java',encoding='utf-8') as op_file:
        for line in op_file:
            print(line.rstrip())
    # with open('D:/desktop/hello.txt') as op_file1:
    #     lines = op_file1.readlines()
    # for line in lines:
    #     print(line.rstrip())

if __name__ == '__main__':
    main()