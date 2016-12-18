#!/usr/bin/python3
import sys
import re

i=1
for line in sys.stdin:
	if i==1:
		print (line[:-1])
		i=2
	else:
		i=1
