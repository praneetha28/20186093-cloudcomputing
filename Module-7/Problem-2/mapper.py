#!/usr/bin/env python

import json
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = json.loads(line.decode("utf-8"))
    key = line[0].strip()
    value = line[1].strip()
    print '%s%s' %(key+"\t", line)
        
