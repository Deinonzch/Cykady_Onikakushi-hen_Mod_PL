#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from operator import itemgetter
import re

reg = re.compile(r'NULL, (\"(?!\\n)[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9\.\\:,\s\'\?\!\-—\(\)~☆♪&*=+;><"]+(\.|\?|\'|\!|,|\\|—|-|\"|~|\)|☆|♪|&|\*|[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9])\")')

f = open('onik_014.txt', 'r')
g = open('onik_014_pl.txt', 'r')
#f = open('onik_tips_18.txt', 'r')
#g = open('onik_tips_18_pl.txt', 'r')
lines = g.readlines()
i=0
for line in f:
  if re.findall(reg, line):
    #print (line[:-1])
    for match in re.findall(reg, line):
      print(line.replace(match[0], lines[i][:-1])[:-1])
      i += 1
  else:
    print (line[:-1])
f.close()
g.close()

