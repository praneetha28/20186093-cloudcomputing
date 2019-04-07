#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
import json
import ast


order = {}
line_item={}

def create(key, value):
    if(key == 'order'):
        order[str(value[1])] = value
    else:
        if value[1] not in line_item.keys():
            line_item[str(value[1])] = [value]
        else:
            line_item[str(value[1])].append(value)
            



def final_list(order, line_item):
    list1 = []
    for i in line_item.keys():
        for j in order.keys():
            if i == j:
                for k in line_item[j]:
                    list1 = []
                    list1.append(order[j])
                    list1.append(k)
                    print list1

# input comes from STDIN

count = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split("\t", 1)
    new_val = value.split(", ")
    create(key, new_val)


final_list(order, line_item)

    