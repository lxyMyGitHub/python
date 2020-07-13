# 导入mysql工具类 *
import jdReptile.mysqlHelper as sqlHelper
import csv
# 随机数工具类
import uuid
# 导入爬虫工具类 *
import jdReptile.getComment as comment
# 导入词云工具类 *
import jdReptile.wordCloudUtil as WCUtil

# 初始化数据字典 False不初始化
def intiDictForMysql(initFlag):
    if initFlag == False : return
    typeMap = {
        '金领冠系列': 'Y001',
        '珍护': 'Y002',
        '菁护': 'Y003',
        '睿护': 'Y004',
        '沛能': 'Y005',
        '有机': 'Y006'
    }
    db = sqlHelper.getDB()
    sqlHelper.saveMapAsTable(db,typeMap,"dictionary")
    sqlHelper.closeDB(db)
    print("init Dictionary is successful")

# 初始化待爬数据
def skuDataInit(initFlag):
    if initFlag == False: return
    f = open('skuData.csv',encoding='utf-8')
    reader = csv.reader(f)
    db = sqlHelper.getDB()
    cursor = sqlHelper.getCursor(db)
    for row in reader:
        sql = "insert into skuData (id,content,sku,dictType) values ('{}','{}','{}','{}')".format(
            uuid.uuid1(),row[0],row[1],row[2]
        )
        cursor.execute(sql)
    db.commit()
    sqlHelper.closeDB(db)



print('start')

# 初始化数据字典
intiDictForMysql(False)

# 初始化待爬数据
skuDataInit(False)

# 爬取&入库
comment.reptileForMysql(False)

# 生成词云,保存到wordCloudOut路径下
WCUtil.createWordCloud()
WCUtil.createAllWordCloud()
print('the end')