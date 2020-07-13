# -*- coding:utf-8 -*-
import matplotlib.pyplot as  plt
import pandas as pd
import numpy as np
import warnings
# seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，
# 在大多数情况下使用seaborn就能做出很具有吸引力的图，
# 而使用matplotlib就能制作具有更多特色的图。应该把Seaborn视为matplotlib的补充，而不是替代物。
import seaborn as sns
#线性回归分析 ,导包
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#标准化
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
# 设置颜色和风格
color=sns.color_palette()
# 设置图形风格调整参数
sns.set_style('darkgrid')

# 警告忽略
def ignore_warn(*args,**kwargs):
    pass
warnings.warn=ignore_warn

# 读取数据,
df=pd.read_csv("data/data.csv",index_col=0)
print(df.head())
print(df.info())

# 了解数据分布,大小的情况, 描述数据,
# 盘点数据是否符合数业务场景, 确认数据与真实数据一致
des = df.describe()
print(des)
# 相关与可视化
# 研究相关: 有两种方法   第一种df.corr() 两两组合,研究相关性大小
corr = df.corr()
print(corr)

# 日期,总计,面条/粥,钙铁锌/维生素,米粉/菜粉,宝宝零食,婴儿尿裤,拉拉裤,儿童餐具,牙胶安抚,奶瓶奶嘴,水壶水杯,洗发沐浴,宝宝护肤,日常护理,驱蚊防晒
# date,sum,field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14
# 相关与可视化
# 问题是,预测y ,那么就要寻找y和x之间的变量关系
# 查看任意两两变量之间的相关性,主要目的是预测销售额,所以取出revenue列,排序

# 如果觉得第一种太杂乱, 就选用这种, 可以选定出只看跟revenue有关

corr_sum = df.corr()[['sum']].sort_values(by='sum',ascending=False)
# 从高到低排序
print(corr_sum)

# 相关性弱, 不要过度解读正负关系, 不要因为这个去作为业务的判断, 相关性收到数据量等方面的数据
# 回归,预测等, 数据颗粒度越细越好,数据越全越好
# 热力图,
heatmap = sns.heatmap(corr)
plt.show()
# 线性相关性可视化
# regplot 做线性回归的拟合 方法是x在前,Y在后
for i in range(1,15):
    fieldName = 'field' + str(i)
    sns.regplot(fieldName,'sum',data=df)
    plt.show()


print('相关度前三和最低分别为:')
print('top1:钙铁锌/维生素,field2,0.981124')
print('top2:米粉/菜粉,field3,0.975038')
print('top3:奶瓶奶嘴,field9,0.973710')
print('top14:驱蚊防晒,field14,0.556965')






'''
#建立自变量和因变量
x=df[['field1','field2','field3','field4','field5','field6','field7','field8','field9','field10','field11','field12','field13','field14']]
y=df['sum'].values

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.25)

#对训练集和测试集特征值进行标准化
std=StandardScaler()
x_train=std.fit_transform(x_train)
x_test=std.transform(x_test)
std_y=StandardScaler()
# ValueError: Expected 2D array, got 1D array instead: transform(二维数组参数)
# 传递了一维数组会报这个错误
# 解决方法 使用数组的reshape()方法,将一维数组转换成二维数组
y_train=std_y.fit_transform(y_train.reshape(-1,1))
y_test=std_y.transform(y_test.reshape(-1,1))

# 4:进行算法流程
# 建模:建立一个空的线性回归模型
model = LinearRegression()

# fit predict score
model.fit(x_train, y_train)

# 系数
coef = model.coef_
print(coef)
# 截距
intercept = model.intercept_
print(intercept)

# 预测
y_predict=std_y.inverse_transform(model.predict(x_test))
print('模型预测: ')
print(y_predict)
# 模型得分
modelScore = model.score(x_test,y_test)
print('模型得分: '+str(modelScore))

# 回归模型评估
#     核心就是看residual(参差) 预测值和真实值之间的差距  计算出真实值和预测值之间的差
#     怎么去计算呢?

#     MAE(平均绝对误差)
#     RMSE(均方根误差)


x2=sm.add_constant(x)
model2=sm.OLS(y,x2).fit()
summary = model2.summary()
print(summary)'''
