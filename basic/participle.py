# coding: utf-8

'''
5.输入一个中文序列，返回有意义的词语序列。分词的规则：
（1）根据词典表中的词进行分割，如果不在词典中则作为单字返回。
（2）如果词典表中的词有冲突，则取最长的词作为结果。
比如输入的中文序列是“就读于北京大学”，词典表中只有三个词，分别是“北京”、“大学”，“北京大学”，那就返回['就','读','于','北京大学']
（3）词典表见群中的文件：CoreNatureDictionary.mini.txt
分词示例：
输入中文序列：”李明出生于上海，现在就读于北京大学”
输出词语列表：['李', '明', '出生于', '上海', '，', '现在', '就读', '于', '北京大学']
'''


def read_txt(name):
    with open(name, 'r') as file_obj:
        for line in file_obj:
            yield line

dictionary = read_txt("CoreNatureDictionary.mini.txt")
string = ''
for d in dictionary:
    string += d
set_list = eval(string)

chinese = "李明出生于上海，现在就读于北京大学"
dict_list = {s: chinese.find(s) for s in set_list if chinese.find(s) > 0}
rev_dict = {}
for k, v in dict_list.items():
    rev_dict.setdefault(v, set()).add(k)
ch_list = []
i = 0
while i < len(chinese):
    if i not in rev_dict:
        ch_list.append(chinese[i])
        i += 1
    else:
        ch = max(rev_dict.get(i), key=len)
        ch_list.append(ch)
        i += len(ch)
print(ch_list)
