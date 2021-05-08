# coding: utf-8

'''
二、numpy练习
2、a=np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])
1）通过numpy切片如何获取切片后的数组为b=np.array([1,3],[9,11])
2）c=a[1::2,:2],c 的结果为？
3）获取a数组中大于4的索引
4）分别计算a数组中行，列的最小值。
'''

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#print(a)

b=a[0:3:2,0:3:2]
print(b)

c=a[1::2,:2]
print(c)

y=np.where(a>4)
print(y)

print(np.amin(a,axis=1))
print(np.amin(a,axis=0))
