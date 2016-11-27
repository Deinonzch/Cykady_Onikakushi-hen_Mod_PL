#!/usr/bin/python3
import sys
import re

i=1
for line in sys.stdin:
	if i==2:
		print (line[:-1])
		i=1
	else:
		i=2