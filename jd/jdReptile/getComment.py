# -*- coding:utf-8 -*-
# 导入requests模块
import requests as re
# 导入json模块
import json
import jdReptile.mysqlHelper as sqlHelper
import uuid
import time
import jdReptile.headerUtil as headerUtil

# 获取评论并保存
def getContentAndSave(sku,dictType,db,maxPageNum):
    headers = headerUtil.getHeaders()
    cursor = db.cursor()
    for pageNum in range(0,maxPageNum):
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(
            sku,pageNum
            )

        # 每爬十页切换一个浏览器版本信息,防封
        if pageNum%10 ==0:
            headers = headerUtil.getHeaders()
        # 获取url中的所有信息
        req = re.get(url, timeout=30, headers=headers)
        # 响应信息为空,长度小于1,不处理
        if len(req.content) < 1:
            return
        # 先把不用的内容去掉，再用json库解析它，得到我们想要的内容
        jdMessages = json.loads(req.text.lstrip("fetchJSON_comme rstrip nt98vv375(").rstrip(");"))
        # 遍历 message
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
    # 更新sku爬取数据状态信息
    updateSql = "update skuData set status = 1 where sku = '{}'".format(sku)
    cursor.execute(updateSql)
    db.commit()

# 爬取京东评论
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
