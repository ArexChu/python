# coding: utf-8

'''
三、Pandas练习
1、读取csv文件数据，数据格式如下表
城市	薪资	房价	人数
北京	10000	54670	200000
上海	9800	48060	180000
深圳	11000	47000	150000
2、使用pandas计算
1）三个城市的平均薪资，平均房价，平均人数
2）计算薪资最高城市，房价最低的城市，人数最少的城市
3）筛选出房价大于48000的城市
4）使用索引只有城市和人数的数据
'''

import pandas as pd

data = pd.read_csv('data.csv')
frame = pd.DataFrame(data)
print(frame)

print("三个城市的平均薪资:%f,平均房价:%f,平均人数:%d"%(frame.薪资.mean(),frame.房价.mean(),frame.人数.mean()))

print("薪资最高城市:%s,房价最低的城市:%s,人数最少的城市:%s"%(frame.iloc[:,0][frame.薪资 == frame.薪资.max()].values[0],frame.iloc[:,0][frame.房价 == frame.房价.min()].values[0],frame.iloc[:,0][frame.人数 == frame.人数.min()].values[0]))

print("房价大于48000的城市:%s"%frame.iloc[:,0][frame.房价 > 48000].values[0])

print(frame.iloc[:,[0,3]])
