# -*- coding:utf-8 -*-

# 导入mysql
import pymysql
# 导入UUID
import uuid

def getDB():
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "root", "idolidea")
    return db

def saveMapAsTable(db,map,tableName):
    cursor = db.cursor()
    for k in map.keys():
        print(k, map[k])
        uuidStr = uuid.uuid1()
        sql = "insert into dictionary(id,name,type) values ('{}','{}','{}')".format(uuidStr,k,map[k])
        print(sql)
        cursor.execute(sql)
    db.commit()

def getCursor(db):
    return db.cursor()

def queryfetchall(db,sql):
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
def closeDB(db):
    # 关闭数据库连接
    db.close()