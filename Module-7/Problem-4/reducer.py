#!/usr/bin/env python

from operator import itemgetter
import sys

friends = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[1] = words[1].strip("]")
    words[1] = words[1].strip("\"")
    
    if words[0] not in friends.keys():
        friends[words[0]] = [words[1]]
    else:
        friends[words[0]].append(words[1])

for i in friends.keys():
    for j in friends[i]:
        if j in friends.keys():
            if i in friends[j]:
                friends[j].remove(i) 
                friends[i].remove(j)

for k in friends.keys():
    for l in friends[k]:
        print [l, k]
        print [k ,l]            