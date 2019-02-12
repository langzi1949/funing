# coding = utf-8
import configparser

def main():
    cf = configparser.ConfigParser()
    print(cf)
    cf.read('config.properties')
    print(cf.sections())

if __name__ == '__main__':
    main()