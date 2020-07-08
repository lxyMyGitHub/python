import PIL.Image as image
from wordcloud import WordCloud
import jieba
import jdReptile.mysqlHelper as sqlHelper
import  numpy as np

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
    stopwords = ['宝宝','京东']
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







