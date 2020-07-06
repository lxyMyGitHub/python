import jdReptile.mysqlHelper as sqlHelper
import csv
import uuid
import jdReptile.getComment as comment
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




# 初始化数据字典
intiDictForMysql(False)
# 初始化待爬数据
skuDataInit(False)
# 爬取&入库
comment.reptileForMysql()