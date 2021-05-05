#coding: utf-8

'''
3.异常捕捉练习： 
2）加法计算器：将编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
'''

while True:
    try:
        number1 = int(input("please input the first number:"))
        number2 = int(input("please input the sencond number:"))
    except ValueError:
        print("the input is not the number!")
    else:
        print("the sum of the two number is %d"%(number1+number2))
        break
