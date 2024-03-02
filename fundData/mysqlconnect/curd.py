import pymysql
import pprint
import os
import yaml

# path_config = r"/fundData/mysqlconnect/config.yml"
# with open(os.path.expanduser(path_config), "r") as config:
#     cfg = yaml.safe_load(config)

curPath = os.path.dirname(os.path.relpath(__file__))
ymlPath = os.path.join(curPath, "config.yml")

with open(os.path.expanduser(ymlPath), "r") as config:
    cfg = yaml.safe_load(config)
    mysqlInfo = cfg.get('mysql')
    parameter = mysqlInfo.get('parameter')

conn=pymysql.connect(host = mysqlInfo.get('host') # 连接名称，默认127.0.0.1
,user = mysqlInfo.get('user')
,passwd = mysqlInfo.get('password')
,port = mysqlInfo.get('port')
,db = mysqlInfo.get('database')
,charset = parameter.get('charset')
)

cur = conn.cursor()

