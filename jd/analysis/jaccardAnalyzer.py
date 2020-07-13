from analysis.similaritymeasures import Similarity
import csv



top1Data = csv.reader('data/top1.csv')
top1AllData = csv.reader('data/top1All.csv')
top14Data = csv.reader('data/top14.csv')
top14AllData = csv.reader('data/top14All.csv')
measures = Similarity()

keys = ['年龄','性别','常用收货省份','会员级别','学历','用户月支付订单总额']
# 维生素
# 驱蚊防晒
f1 = open('data\\top1.csv',encoding='utf-8')
f2 = open('data\\top1All.csv',encoding='utf-8')
f3 = open('data\\top14.csv',encoding='utf-8')
f4 = open('data\\top14All.csv',encoding='utf-8')
ageA = []
genderA = []
cityA = []
vipA = []
educationA = []
amountA = []

ageB = []
genderB = []
cityB = []
vipB = []
educationB = []
amountB = []

rows = csv.reader(f1, delimiter=',')
number = 0
for row in rows:
    for r in row:
        if number == 0:
            ageA.append(r)
        if number == 1:
            genderA.append(r)
        if number == 2:
            cityA.append(r)
        if number == 3:
            vipA.append(r)
        if number == 4:
            educationA.append(r)
        if number == 5:
            amountA.append(r)
    number = number + 1
listA = [ageA,genderA,cityA,vipA,educationA,amountA]
# print(listA)

rows = csv.reader(f2, delimiter=',')
number = 0
for row in rows:
    for r in row:
        if number == 0:
            ageB.append(r)
        if number == 1:
            genderB.append(r)
        if number == 2:
            cityB.append(r)
        if number == 3:
            vipB.append(r)
        if number == 4:
            educationB.append(r)
        if number == 5:
            amountB.append(r)
    number = number + 1
listB = [ageB,genderB,cityB,vipB,educationB,amountB]
# print(listB)

# Top1 jaccard
print('Top1 维生素 jaccard')
for i in range(0,6):
    key = keys[i]
    A = listA[i]
    B = listB[i]
    print(key+' : '+str(measures.jaccard_similarity(A, B)))



ageA = []
genderA = []
cityA = []
vipA = []
educationA = []
amountA = []

ageB = []
genderB = []
cityB = []
vipB = []
educationB = []
amountB = []

rows = csv.reader(f3, delimiter=',')
number = 0
for row in rows:
    for r in row:
        if number == 0:
            ageA.append(r)
        if number == 1:
            genderA.append(r)
        if number == 2:
            cityA.append(r)
        if number == 3:
            vipA.append(r)
        if number == 4:
            educationA.append(r)
        if number == 5:
            amountA.append(r)
    number = number + 1
listA = [ageA,genderA,cityA,vipA,educationA,amountA]
# print(listA)



rows = csv.reader(f4, delimiter=',')
number = 0
for row in rows:
    for r in row:
        if number == 0:
            ageB.append(r)
        if number == 1:
            genderB.append(r)
        if number == 2:
            cityB.append(r)
        if number == 3:
            vipB.append(r)
        if number == 4:
            educationB.append(r)
        if number == 5:
            amountB.append(r)
    number = number + 1
listB = [ageB,genderB,cityB,vipB,educationB,amountB]
# print(listB)

# Top14 jaccard
print('Top14 驱蚊防晒 jaccard')
for i in range(0,6):
    key = keys[i]
    A = listA[i]
    B = listB[i]
    print(key+' : '+str(measures.jaccard_similarity(A, B)))