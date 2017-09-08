#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re

for line in sys.stdin:
	words = re.findall(r'(\"[A-Za-zĘÓŁŚĄŻŹĆŃęółśążźćń0-9\.\\:,\s\'\?\!\-—\(\)~☆♪「」*=+;"]+(\.|\?|\'|\!|,|\\|—|-|\"|~|\)|☆|♪|\*)\")',line)
	if words:
		print(words[0][0] + "\n")
