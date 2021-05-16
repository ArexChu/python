# coding: utf-8

'''
爬取https://www.ivsky.com/tupian/ziranfengguang/ 自然风光下所有页面数据

爬虫字段  图片名，图片url两个字段保存到txt文件

图片保存到image文件夹中

注意：分别使用正则和xpath两种方式爬取
'''

#正则

import requests
import re
import os

images = "images"
if not os.path.exists(images):
    os.mkdir(images)

for i in range(1,113):
    urls = 'https://www.ivsky.com/tupian/ziranfengguang/index_{}.html'.format(i)
    res = requests.get(urls)

    pattern = re.compile(r'target="_blank"><img src="(.*?)" alt=')
    urls = pattern.findall(res.text)
    https_urls = ["https:"+i for i in urls]
    pattern = re.compile(r'" alt="(.*?)"></a>')
    name = pattern.findall(res.text)
    
    with open('pic_info.txt','a') as f:
        for i in range(len(name)):
            f.write(name[i] + ',' + https_urls[i] + '\n')
    
    for i in https_urls:
        pic_file_path = os.path.join('images',i.split('/')[-1])
        pic = requests.get(i)
        with open(pic_file_path,'wb') as f:
            f.write(pic.content)
