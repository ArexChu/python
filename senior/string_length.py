# coding: utf-8

'''
一、编程逻辑
2、给定一个字符串，找出不含有重复字符的最长子串的长度和最长字符串。
示例：
给定“abcabcbb”，最长子串是“abc”，”bca”,”cab”，那么长度就是3。
给定“bbbbb”，最长的子串就是“b”，长度是1。
给定“pwwkew”，最长子串是“wke”，“kew”，长度是3。
'''

'''
思路：
从第一个字母开始，下标向右移动，每新增一个字母和前面所有字母对比是否重复，如果重复，则记录该子串及其长度，并从该字母开始向右移动，否则继续直到下标到达字符串尾部
'''

string = input("请输入一个字符串：")
string_list = [""]

def add_longest_string(string):
    if len(string) > len(string_list[0]):
        string_list.clear()
        if string not in string_list:
            string_list.append(string)
    elif len(string) == len(string_list[0]):
        if string not in string_list:
            string_list.append(string)

for start_letter in range(len(string)):
    for index in range(start_letter+1,len(string)):
        if string[index] in string[start_letter:index]:
            add_longest_string(string[start_letter:index])
            break
        elif index == len(string)-1:
            add_longest_string(string[start_letter:len(string)])

print("最长子串是%s，长度是%d。"%(string_list,len(string_list[0])))
