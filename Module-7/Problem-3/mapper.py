#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	word = line.split(", ")
	word[0] = word[0].strip("[")
	word[0] = word[0].strip("\"")
	print '%s\t%s' % (word[0], 1)