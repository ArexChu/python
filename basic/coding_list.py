#coding: utf-8

'''
2. 文件操作练习：
5）.关于编程的调查：编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
'''

def write_file(name,content):
    with open(name,'a') as file_obj:
        file_obj.write(content)

while True:
    reason = input("please input why you like coding?:")
    reason_line = reason + '\n'
    write_file("coding_reasons.txt",reason_line)

