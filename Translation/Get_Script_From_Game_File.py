#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re

for line in sys.stdin:
	words = re.findall(r'NULL, (\"(?!\\n)[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9\.\\:,\s\'\?\!\-—\(\)~☆♪「」*=+;><"]+(\.|\?|\'|\!|,|\\|—|-|\"|~|\)|☆|♪|\*|[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9])\")',line)
	if words:
		print(words[0][0] + "\n")
