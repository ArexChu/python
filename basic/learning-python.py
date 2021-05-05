#coding: utf-8

'''
2. 文件操作练习：
1）.在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python 知识，其中每一行都以“In Python you can”打头。将这个文件命名为learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中。
'''

with open("learning_python.txt",'w') as file_obj:
    summary = "In Python you can read words in the file.\nIn Python you can calculate the sum of the numbers.\n" 
    file_obj.write(summary)

with open("learning_python.txt",'r') as file_obj:
    print(file_obj.read())

with open("learning_python.txt",'r') as file_obj:
    for line in file_obj:
        print(line,end="")
    print()

with open("learning_python.txt",'r') as file_obj:
    print(file_obj.readlines())
    print()

'''
2）.下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'： >>> message = "I really like dogs." >>> message.replace('dog', 'cat') 'I really like cats.' 读取你刚创建的文件learning_python.txt 中的每一行，将其中的Python 都替换为另 一门语言的名称，如C。将修改后的各行都打印到屏幕上。块外打印它们。
'''

with open("learning_python.txt",'r') as file_obj:
    for line in file_obj:
        print(line.replace('Python','C'),end="")
