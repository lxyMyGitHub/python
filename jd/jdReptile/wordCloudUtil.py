# coding=UTF-8
import PIL.Image as image
from wordcloud import WordCloud
import jieba
import jdReptile.mysqlHelper as sqlHelper
import numpy as np

# 中文结巴分词切分
def transCN(words,text):
    cuts = jieba.cut(text)
    for cut in cuts:
        words.append(cut)
    return words



# 读取数据分别生成词云
def createWordCloud():
    db = sqlHelper.getDB()
    queryTypesSql = 'select type,name from dictionary'
    typeRes = sqlHelper.queryfetchall(db,queryTypesSql)
    # 遮罩图片
    mask = np.array(image.open("timg1.jpg"))
    # 屏蔽词
    stopwords = ['宝宝','京东','奶粉','孩子','这个','伊利',
                '宝贝','购买','可以','非常','一直','好评','这个','其他',
                '一直','现在','而且','我们','因为','所以','没有','金领',
                '小孩','这个','这次','就是','觉得','什么','这款','之前',
                '我家','东西','但是','已经','以前','以后','真的']
    for row in typeRes:
        showWords = []
        queryContents = 'select content from jdcontents where dictType = "{}"'.format(
            row[0]
        )
        contents = sqlHelper.queryfetchall(db,queryContents)
        for contentRow in contents:
            content = contentRow[0]
            showWords = transCN(showWords,content)
        wordCloud = WordCloud(
                        font_path='msyh.ttc',
                        background_color='white',
                        width=1000,
                        height=800,
                        stopwords=stopwords,
                        mask=mask,
                        max_words=3000,
                        random_state=200,
                        min_font_size=15,
                        max_font_size=80,
                        collocations=False
                    ).generate(" ".join(showWords))
        imageFile = wordCloud.to_image()
        #imageFile.show()
        wordCloud.to_file('wordCloudOut\\'+row[1]+'.jpg')
        print(row[1]+'词云生成成功!')
    sqlHelper.closeDB(db)


# 读取数据生成总词云
def createAllWordCloud():
    db = sqlHelper.getDB()
    # 遮罩图片
    mask = np.array(image.open("timg1.jpg"))
    # 屏蔽词
    stopwords = ['宝宝','京东','奶粉','孩子','这个','伊利',
                '宝贝','购买','可以','非常','一直','好评','这个','其他',
                '一直','现在','而且','我们','因为','所以','没有','金领',
                '小孩','这个','这次','就是','觉得','什么','这款','之前',
                '我家','东西','但是','已经','以前','以后','真的']
    showWords = []
    queryContents = 'select content from jdcontents'
    contents = sqlHelper.queryfetchall(db,queryContents)
    for contentRow in contents:
        content = contentRow[0]
        showWords = transCN(showWords,content)
    wordCloud = WordCloud(
                    font_path='msyh.ttc',
                    background_color='white',
                    width=1000,
                    height=800,
                    stopwords=stopwords,
                    mask=mask,
                    max_words=3000,
                    random_state=200,
                    min_font_size=15,
                    max_font_size=80,
                    collocations=False
                ).generate(" ".join(showWords))
    imageFile = wordCloud.to_image()
    #imageFile.show()
    wordCloud.to_file('wordCloudOut\\'+'all.jpg')
    print('总词云生成成功!')
    sqlHelper.closeDB(db)
    print('单词计数开始')
    stopwords.extend(['，', '。', '：', '、', '！', '；', ' ', '？'])
    wordCount(showWords,stopwords,1000)
    print('单词计数结束')

# 单词计数
def wordCount(words,stopwords,topNum):
    wcDict = {}
    for word in words:
        if word in stopwords:
            continue
        if word in wcDict.keys():
            wcDict[word] = wcDict[word]+1
        else:
            wcDict[word] = 1
    count_list=sorted(wcDict.items(),key=lambda x:x[1],reverse=True)
    # print(count_list)
    filename = 'wordCountOut/wordcount.txt'
    with open(filename, 'w',encoding='utf-8') as file:
        countNumber = 0
        for countKey in count_list:
            if countNumber >= topNum:
                break
            # print(countKey[0]+' : '+str(countKey[1]))
            file.write(countKey[0]+' : '+str(countKey[1])+'\n')
            countNumber = countNumber + 1








