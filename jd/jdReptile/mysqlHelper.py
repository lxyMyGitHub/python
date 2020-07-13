# -*- coding:utf-8 -*-

# 导入mysql
import pymysql
# 导入UUID
import uuid

# 获取数据库连接
def getDB():
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "idolidea", "123456", "idolidea")
    return db

# 数据字典存储到mysql
def saveMapAsTable(db,map,tableName):
    cursor = db.cursor()
    for k in map.keys():
        print(k, map[k])
        uuidStr = uuid.uuid1()
        sql = "insert into dictionary(id,name,type) values ('{}','{}','{}')".format(uuidStr,k,map[k])
        print(sql)
        cursor.execute(sql)
    db.commit()

# 获取游标
def getCursor(db):
    return db.cursor()

# 查询并返回所有结果集
def queryfetchall(db,sql):
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

# 关闭数据库连接
def closeDB(db):
    db.close()