# coding = utf-8
import configparser
import pymysql
import os,sys

def get_conf():
    return configparser.ConfigParser()

def get_risk_conn():
    #get config info from config file
    cf = get_conf()
    path = os.path.split(os.path.realpath(__file__))[0]
    cf.read(path + '/config.properties')
    #print(cf.sections())
    # return mysql-connection
    return pymysql.connect(host=cf.get('risk','risk.host'),port=cf.getint('risk','risk.port'),\
                    user=cf.get('risk','risk.user'),passwd=cf.get('risk','risk.passwd'),\
                    db=cf.get('risk','risk.db'),charset=cf.get('risk','risk.charset'))

def get_prod_risk_conn():
    cf = get_conf()
    path = os.path.split(os.path.realpath(__file__))[0]
    cf.read(path + '/config.properties')
    return pymysql.connect(host=cf.get('prod_risk','prod_risk.host'),port=cf.getint('prod_risk','prod_risk.port'),\
                    user=cf.get('prod_risk','prod_risk.user'),passwd=cf.get('prod_risk','prod_risk.passwd'),\
                    db=cf.get('prod_risk','prod_risk.db'),charset=cf.get('prod_risk','prod_risk.charset')) 