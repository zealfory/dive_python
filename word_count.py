# -*- encoding: utf-8 -*-
# @File:   word_count.py    
# @Time: 2020-05-21 16:06
# @Author: ZHANG
# @Description: word_count

from collections import Counter
import re


def creat_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(" "))
    return datalist


def wc(filename):
    print(Counter(creat_list(filename)))


if __name__ == "__main__":
    filename = 'test.txt'
    wc(filename)

