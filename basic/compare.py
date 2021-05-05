#coding: utf-8

a = input("please input a:")
b = input("please input b:")
c = input("please input c:")

if (a >= b):
    if(c >= a):
        print(c)
    else:
        print(a)
else:
    if(c >= b):
        print(c)
    else:
        print(b)
