#!/usr/bin/python3
import sys
import re

tab_line = []

pattern1 = re.compile(r'\"[^\"\\]+\"')
pattern2 = re.compile(r'\"\\\"[^\"\\]+\"')
pattern3 = re.compile(r'\"[^\"\\]+\\\"\"')
pattern4 = re.compile(r'\"\\\"[^\"\\]+\\\"\"')

correct_sentence = ""
check_sentence = ""

for line in sys.stdin:
	tab_line.append(line)

for index, line in enumerate(tab_line):
	if index%2 == 0:
		correct_sentence = line
	else:
		check_sentence = line
		if re.search(pattern4, correct_sentence):
			if re.search(pattern4, check_sentence):
				print(str(index) + " Good")
			else:
				print(str(index) + " Should be \"\\\"somethink\\\"\"")
		else:
			if re.search(pattern3, correct_sentence):
				if re.search(pattern3, check_sentence):
					print(str(index) + " Good")
				else:
					print(str(index) + " Should be \"somethink\\\"\"")
			else:
				if re.search(pattern2, correct_sentence):
					if re.search(pattern2, check_sentence):
						print(str(index) + " Good")
					else:
						print(str(index) + " Should be \"\\\"somethink\"")
				else:
					if re.search(pattern1, correct_sentence):
						if re.search(pattern1, check_sentence):
							print(str(index) + " Good")
						else:
							print(str(index) + " Should be \"somethink\"")