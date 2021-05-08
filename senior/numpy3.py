# coding: utf-8

'''
二、numpy练习
3、a = np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])
如何实现a数组的转置，请用多种方法实现
'''

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a.T)
print(a.swapaxes(0,1))
print(a.transpose(1,0))
