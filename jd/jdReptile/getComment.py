# -*- coding:utf-8 -*-
# 导入requests模块
import requests as re
# 导入json模块
import json
import random
# 导入CSV安装包
import csv
import jdReptile.mysqlHelper as sqlHelper
import uuid
import time
import jdReptile.headerUtil as headerUtil


def getContentAndSave(sku,dictType,db,maxPageNum):
    headers = headerUtil.getHeaders()
    cursor = db.cursor()
    for pageNum in range(0,maxPageNum):
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(
            sku,pageNum
            )
        # 获取url中的所有信息
        if pageNum%10 ==0:
            headers = headerUtil.getHeaders()
        req = re.get(url, timeout=30, headers=headers)
        if len(req.content) < 1:
            return
        # 先把不用的内容去掉，再用json库解析它，得到我们想要的内容
        jdMessages = json.loads(req.text.lstrip("fetchJSON_comme rstrip nt98vv375(").rstrip(");"))
        for msg in jdMessages['comments']:
            content = msg['content'].replace('\n', '').replace('\r', '').replace('\'',' ')
            # print(dictType+" : "+content)
            uuidStr = uuid.uuid1()
            sql = "insert into jdContents(id,sku,dictType,content) values ('{}','{}','{}','{}')".format(
                uuidStr,sku,dictType,content
            )
            cursor.execute(sql)
        db.commit()

        print("sku : ",sku,"page 进度 :", pageNum ," 共:",maxPageNum,"sleep 2 s")
        time.sleep(2)
    updateSql = "update skuData set status = 1 where sku = '{}'".format(sku)
    cursor.execute(updateSql)
    db.commit()


def reptileForMysql(initFlag):
    if initFlag : return
    maxPageNum = 30
    db = sqlHelper.getDB()
    sql = "select sku,dictType from skuData where status = 0"
    res = sqlHelper.queryfetchall(db,sql)
    number = 0
    for row in res:
        sku = row[0]
        dictType = row[1]
        getContentAndSave(sku,dictType,db,maxPageNum)
        number = number+1
        print("============ sku :", sku, "爬取存储完成,已完成: ", number)
        time.sleep(30)
    sqlHelper.closeDB(db)
    print("完成")
