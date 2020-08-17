# -*- encoding: utf-8 -*-
# @File:   get_images.py    
# @Time: 2020-05-27 14:19
# @Author: ZHANG
# @Description: 获取镜像列表

import os
import yaml
import re


s = set()


def EnumPathFiles(path, callback):
    if not os.path.isdir(path):
        print('file:', path)
        return
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:
        for d in dirs:
            EnumPathFiles(os.path.join(root, d), callback)
        for f in files:
            callback(root, f)


def callback1(path, filename):
    f = str(path + os.sep +filename)
    # print('path', f)
    if f.endswith('.yaml'):
        with open(f) as ff:
            dict_yaml = yaml.load_all(ff)
            for doc in dict_yaml:
                doc = str(doc)
                x = doc.find("gcr.io")
                if x != -1:
                    tmp = re.split('[\'|\"|\\n]', doc[x:])[0]
                    s.add(tmp)
                    # print(tmp)
                    # if tmp != "image:":
                    #     print(tmp)
                    # else:
                    #     tmp = doc[x:].split('\\n')[3]
                    #     print(tmp)


if __name__ == '__main__':
    EnumPathFiles(r'/Users/allen/Downloads/manifests-1.0.2', callback1)
    print("===========================================")
    for i in s:
        print(i)

