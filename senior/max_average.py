# coding: utf-8

'''
一、编程逻辑
3、给定一个序列，计算任意个连续元素的最大平均值和其中的元素。
示例：
输入:序列list=[1,2,3,3,4,8,5,7],k=2
输出：最大平均值：（8+5）/2=6.5   元素为：[8,5]

输入:序列list=[1,2,3,5,4],k=3
输出：最大平均值：（3+5+4）/3=4   元素为：[3,5,4]

输入:序列list=[1,10,2,5,4],k=2
输出：最大平均值：（10+2）/2=6   元素为：[10,2]
'''

'''
思路：
下标从0开始移动，每个开始下标都遍历至末尾
'''

num_list = eval(input("请输入一个序列list："))
k = int(input("请输入k："))
length = len(num_list)
ave_max = 0
total = 0
ele_list = []
for start_num in range(length-k):
    total = 0
    for index in range(start_num, start_num+k):
        total = total + int(num_list[index])
    if ave_max <= total/k:
        ave_max = total/k
        ele_list = num_list[start_num:start_num+k]

print("最大平均值：%f 元素为：%s"%(ave_max,ele_list))
