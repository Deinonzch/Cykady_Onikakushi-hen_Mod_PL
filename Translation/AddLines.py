#!/usr/bin/python3

import sys
from operator import itemgetter
import re

reg = re.compile(r'(\"[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9\.\\:,\s\'\?\!\-—\(\)~☆*=+;"]+(\.|\?|\!|,|\\|—|-|\"|~☆*)\")')
regline = re.compile(r'(\sLine.*\);)')

f = open('onik_000.txt', 'r')
g = open('onik_000_pl.txt', 'r')
lines = g.readlines()
i=0
for line in f:
	if re.findall(reg, line):
		matchline = re.findall(regline, line)
		print (line.replace(matchline[0], '')[:-1])
		for match in re.findall(reg, line):
			print(line.replace(match[0], lines[i][:-1])[:-1])
			i += 1
	else:
		print (line[:-1])
		j = 1
f.close()
g.close()
