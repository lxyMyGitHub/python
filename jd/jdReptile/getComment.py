# -*- coding:utf-8 -*-
# 导入requests模块
import requests as re
# 导入json模块
import json
import random
# 导入CSV安装包
import csv

# 把Headers中的Requests URL赋值给url

headers = {'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Request Method':'Get',
            'callback':'fetchJSON_comment98'}

# 数据写入csv文件
# 1. 创建文件对象
f = open('comment.csv', 'w', encoding='utf-8')
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 3. 构建列表头
csv_writer.writerow(["id", "comment"])


# 打印评论信息
def saveComment(url,csv_writer):
    #获取url中的所有信息
    req = re.get(url, timeout=30, headers=headers)
    # print(req.text)
    # 先把不用的内容去掉，再用json库解析它，得到我们想要的内容
    jd=json.loads(req.text.lstrip("fetchJSON_comme rstrip nt98vv375(").rstrip(");"))

    j=1
    for i in jd['comments']:
        csv_writer.writerow([str(j), i['content']])
        # print(str(j)+"、"+i['content'])
        j+=1
    # 关闭数据流
    print("数据持久化成功")
    print("文件流关闭成功")

for i in range(0,1000):
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=3300169&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(i)
    saveComment(url,csv_writer)

f.close()