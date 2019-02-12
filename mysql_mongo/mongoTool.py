#coding=utf-8
import configparser
import os,sys
from pymongo import MongoClient

def get_conf():
    return configparser.ConfigParser()

def get_mongo_connect():
    #get config info from config file
    cf = get_conf()
    path = os.path.split(os.path.realpath(__file__))[0]
    cf.read(path+'/config.properties')
    #return mongodb-connection
    uri = cf.get('mongo','mongo.uri')
    database = cf.get('mongo','mongo.database')
    client = MongoClient(uri)
    db = client[database]
    return db