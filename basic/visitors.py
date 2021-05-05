#coding: utf-8

'''
2. 文件操作练习：
3）.访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt 中。
'''

name = input("please input your names:")

with open("guest.txt",'w') as file_obj:
    file_obj.write(name)
