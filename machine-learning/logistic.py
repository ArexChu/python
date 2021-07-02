# coding: utf-8

'''
用逻辑回归算法和knn算法做分类，并评估哪个模型效果好（计算每个模型的a,p,r,f1）。
训练数据和测试数据在 逻辑回归.xlsx 中。
思路：
1、读取表格数据，训练数据和测试数据
2、使用小批量梯度下降法,根据随机初始化theta，预测y，计算损失值
3、计算目标函数的梯度
4、给定学习率，更新theta，重新预测y，计算损失值， 给定终止条件（超参数）
5、根据训练好的逻辑回归模型对测试数据进行预测,逻辑回归和knn的预测结果和样本真实值生成混淆矩阵，并计算a,p,r,f1
'''

import numpy as np
import pandas as pd

# 1、获取excel数据，存入numpy数组
df_train = pd.read_excel(r'逻辑回归.xlsx', sheet_name= "训练数据")
df_test = pd.read_excel(r'逻辑回归.xlsx', sheet_name= "测试数据")
train = np.array(df_train)
test = np.array(df_test)

# 2、随机初始化theta,预测y
def predict_y(theta, x):
    py1 = 1/(1+np.exp(-np.dot(x, theta)))
    return py1

x = np.column_stack((np.ones(train.shape[0]), train[..., :-1]))
y = train[..., -1]
theta = np.zeros(train.shape[1])

# 3、计算目标函数对theta的偏导数
def gradiet(yp, y, x):
    lp = np.dot((yp - y).T, x)
    return lp

# 4、给定学习率，更新theta，重新预测y
n = 0
while(True):
    yp = predict_y(theta, x)
    lp = gradiet(yp, y, x)
    theta = theta + 0.01 * lp
    n += 1
    if n > 50:
        break

# 5、给定测试集，预测y
xt = np.column_stack((np.ones(test.shape[0]), test[..., :-1]))
ypt = predict_y(theta, xt)
yt = np.where(ypt >= 0.5, 1, 0)
