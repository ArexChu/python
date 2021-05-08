# coding: utf-8

'''
二、numpy练习
1、a=np.arange(10).reshape(2,-1) 
b=np.arange(24).reshape(2,-1,4) 
1）a中的-1代表多少？
5
2）B中的-1代表多少？
3
'''

import numpy as np

a=np.arange(10).reshape(2,-1)
print(a)
b=np.arange(24).reshape(2,-1,4)
print(b)
