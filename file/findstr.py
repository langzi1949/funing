# encoding = utf-8
import os
import re



REGEX ='\w\.java$'
def main(path):
    list_dirs = os.walk(path)
    for root,dirs,files in list_dirs:
        for f in files:
            if re.search(REGEX,f) is not None:
                fname = os.path.join(root,f)
                # encoding open(fname,'r',encoding='utf-8')
                with open(fname,'rb') as open_file:
                    lines = [x.strip() for x in open_file.readlines()]
                for line in lines:
                    #if b'.updateSelective' in line or b'.updateFull' in line:
                    if  b'.updateFull' in line:
                        with open('E:/find_1.txt','a') as wf:
                            wf.write(fname+'\n')

if __name__=='__main__':
    #main('D:\gitlab_workspace')
    main('E:\git_lab')
