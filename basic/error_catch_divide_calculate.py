#coding: utf-8

'''
3.异常捕捉练习： 
3）除法计算器：创建一个只执行除法运算的简单计算器?
'''

while True:
    try:
        dividend = int(input("please input the dividend:"))
        divisor = int(input("please input the divisor:"))
    except ValueError:
        print("the input is not the number!")
    else:
        try:
            quotient = dividend / divisor
        except ZeroDivisionError:
            print("the divisor can't be zero")
        else:
            print("the quotient is %d"%(quotient))
            break
