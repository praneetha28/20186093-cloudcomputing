#!/usr/bin/env python
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # increase counters
    print line