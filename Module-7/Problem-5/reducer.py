#!/usr/bin/env python

from operator import itemgetter
import sys

dna = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[1] = words[1].strip("]")
    words[1] = words[1].strip("\"")
    
    if words[0] not in dna.keys():
        dna[words[0]] = words[1][0:-10]

values = list(dna.values())

value_list = set(values)
for i in value_list:
    print "\""+i+"\""