# coding: utf-8

'''
用knn算法做分类，并评估k值分别为3和5时，哪个模型效果好（计算每个模型的a，p,r,f1）。
训练数据和测试数据在knn.xlsx中。
思路：
1、读取表格数据，训练数据和测试数据
2、从训练集中获取k个离测试集距离最近的训练数据
3、根据获取到的k个训练数据，通过多数表决法来预测测试数据的y值
4、根据模型1、模型2的预测结果和样本真实值生成混淆矩阵，并计算a,p,r,f1
'''

import numpy as np
import pandas as pd

# 1、获取excel数据，存入numpy数组
df_train = pd.read_excel(r'knn.xlsx', sheet_name= "训练数据")
df_test = pd.read_excel(r'knn.xlsx', sheet_name= "测试数据")
train_data = np.array(df_train)
test_data = np.array(df_test)

# 2、计算每个测试数据到训练数据的欧式距离，并获取其中k个最近距离的训练数据
dis = [np.dot(test-train,test-train)**.5 for test in test_data[...,:3] for train in train_data[...,:3]]
dis_res = np.array(dis).reshape((test_data.shape[0],-1))
dis_sort = np.argsort(dis_res)

# 3、多数表决法预测测试集
def predict(k):
    predict = [1 if np.sum(train == 1) > np.sum(train == 0) else 0 for train in train_data[dis_sort[...,:k],3]]
    return predict

module1 = predict(3)
module2 = predict(5)

# 4、生成混淆矩阵，计算a,p,r,f1
def aprf(module):
    data = np.vstack((test_data[...,3],module))
    matrix = np.zeros((2,2), dtype = int)
    for i in range(data.shape[1]):
        if data[0][i] == data[1][i] == 1:
            matrix[0][0] += 1
        if data[0][i] == data[1][i] == 0:
            matrix[1][1] += 1
        if data[0][i] == 1 and data[1][i] == 0:
            matrix[0][1] += 1
        if data[0][i] == 0 and data[1][i] == 1:
            matrix[1][0] += 1
    a = (matrix[0][0] + matrix[1][1])/np.sum(matrix)
    p = matrix[0][0]/(matrix[0][0]+matrix[0][1])
    r = matrix[0][0]/(matrix[0][0]+matrix[1][0])
    f1 = 2*p*r/(p+r)
    return a,p,r,f1

a1,p1,r1,f1 = aprf(module1)
a2,p2,r2,f2 = aprf(module2)
print("k为3时，a1:%s,p1:%s,r1:%s,f1:%s"%(a1,p1,r1,f1))
print("k为5时，a2:%s,p2:%s,r2:%s,f2:%s"%(a2,p2,r2,f2))
