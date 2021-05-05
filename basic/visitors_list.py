#coding: utf-8

'''
2. 文件操作练习：
4）.访客名单：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt 中。确保这个文件中的每条记录都独占一行。
'''

from time import asctime

def write_file(name,content):
    with open(name,'a') as file_obj:
        file_obj.write(content)

while True:
    name = input("please input your name:")
    greeting = "Hi," + name
    print(greeting)
    access_log = str(asctime()) + " " + greeting + '\n'
    write_file("guest_book.txt",access_log)

