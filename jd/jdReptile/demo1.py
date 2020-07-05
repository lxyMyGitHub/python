import requests,json
#url是Headers里的requests URL

url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1072077&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'

#headers的内容在headers里面都可以找到

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Request Method': 'GET',
        'callback':'fetchJSON_comment98'
         }
req=requests.get(url ,timeout=30,headers=headers)
# print(req.text)

# 第二步:解析内容
#先把不用的内容去掉,再用json库去解析, 得到我们想要的东西
jd=json.loads(req.text.lstrip("fetchJSON_comment98(").rstrip(");"))
#通过type(),我们可知jd是一个字典
# print(type(jd))
# print(jd)

# 第三步:通过key来找到所有评论
jd=json.loads(req.text.lstrip("fetchJSON_comment98(").rstrip(");"))
# print(jd['comments'])
# 由图可知，key为 conent 的内容就是我们想要的评价了


# 第四步:遍历输出每一条评价
j=1
for i in jd['comments']:
    print(str(j)+'.'+i['content'])
    j+=1



# # 整合代码
# import requests,json
# url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1072077&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#         'Request Method': 'GET',
#         'callback':'fetchJSON_comment98'
#          }
# # 获取网页信息
# req=requests.get(url,timeout=30,headers=headers)
# # print(req.text)
# #先把不用的内容去掉,再用json库去解析, 得到我们想要的东西
# jd=json.loads(req.text.lstrip("fetchJSON_comment98(").rstrip(");"))
#
# j=1
# for i in jd['comments']:
#     print(str(j)+'.'+i['content'])
#     j+=1


# 词云功能
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import  WordCloud,STOPWORDS
from PIL import Image
j=1
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Request Method': 'GET',
        'callback':'fetchJSON_comment98'
         }
#存放评价
content=[]
def f(url):
    #获取网页信息
    req = requests.get(url, timeout=30, headers=headers)
    #req.text
    #先把不用的内容去掉, 再用json库解析他, 得到我们需要的东西
    jd=json.loads(req.text.lstrip("fetchJSON_comment98(").rstrip(");"))
    #global:声明变量的作用域为全局作用域
    global j
    for i in jd["comments"]:
        content.append(i['content'])

#这里我们只爬取10页作为例子
for i in range(10):
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1072077&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
f(url)
# print(content)

content=''.join(content)
bg_img=np.array(Image.open('../1.jpg'))
wordcloud=WordCloud(font_path='c:/Windows/Fonts/simkai.ttf',stopwords=STOPWORDS).generate(content)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# 存储csv格式
import csv
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
film_title_list=[]
c=open(r'D:\workspaces\demo1\comments.csv','a+',newline='')
fieldnames=content
writer=csv.DictWriter(c,fieldnames=fieldnames)
writer.writeheader()


