#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

a = []
b = []
arow1 = [0,0,0,0,0]
arow2 = [0,0,0,0,0]
arow3 = [0,0,0,0,0]
arow4 = [0,0,0,0,0]
arow5 = [0,0,0,0,0]

brow1 = [0,0,0,0,0]
brow2 = [0,0,0,0,0]
brow3 = [0,0,0,0,0]
brow4 = [0,0,0,0,0]
brow5 = [0,0,0,0,0]



# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[3] = words[3].strip("]")
    words[1] = int(words[1])
    words[2] = int(words[2])
    words[3] = int(words[3])
    
    
    if words[0] == "a":
        if words[1] == 0:
            arow1.insert(words[2],words[3])
        if words[1] == 1:
            arow2.insert(words[2],words[3])
        if words[1] == 2:
            arow3.insert(words[2],words[3])
        if words[1] == 3:
            arow4.insert(words[2],words[3])
        if words[1] == 4:
            arow5.insert(words[2],words[3])
    else:
        if words[1] == 0:
            brow1.insert(words[2],words[3])
        if words[1] == 1:
            brow2.insert(words[2],words[3])
        if words[1] == 2:
            brow3.insert(words[2],words[3])
        if words[1] == 3:
            brow4.insert(words[2],words[3])
        if words[1] == 4:
            brow5.insert(words[2],words[3])
        

a.append(arow1)
a.append(arow2)
a.append(arow3)
a.append(arow4)
a.append(arow5)

b.append(brow1)
b.append(brow2)
b.append(brow3)
b.append(brow4)
b.append(brow5)


result = [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]

for i in result:
    for j in i:
        if j != 0:
            print [result.index(i), i.index(j), j]

