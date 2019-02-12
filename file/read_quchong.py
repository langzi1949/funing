# coding = utf-8
def main():
    set1 = set()
    with open('D:\\desktop\\3.txt',encoding='utf-8') as open_file:
        for line in open_file:
            v = line.strip()
            set1.add(v)
    
    print(len(set1))

    with open('D:\\desktop\\2.txt','w',encoding='utf-8') as write_file:
        for v in set1:
            s = str(v)+'\n'
            write_file.write(s)

if __name__ == '__main__':
    main()