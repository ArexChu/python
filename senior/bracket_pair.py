# coding: utf-8

'''
一、编程逻辑
1、字符串中有括号”()[]{}”，设计一个程序，判断该字符串是否有效
括号必须以正确的顺序配对，如：“()”、“()[]”是有效的，但“([)]”无效。
'''

import re

string = input("请输入字符串：")
# string = "(books)[news]{fruits}"
pattern1 = re.compile(r'\(\w*\)')
result1 = pattern1.findall(string)
pattern2 = re.compile(r'\[\w*\]')
result2 = pattern1.findall(string)
pattern3 = re.compile(r'\{\w*\}')
result3 = pattern1.findall(string)
if len(result1) and len(result2) and len(result3):
    print("该字符串有效")
else:
    print("该字符串无效")
