# coding: utf-8

import os
import shutil

# Flatten folder
# li = os.listdir('.')
# fli = list()
# for fi in li:
#     if os.path.isdir(fi) and 'DS_Store' not in fi:
#     	fli.append(fi)
# for f in fli:
# 	tl = os.listdir(f)
# 	for t in tl:
# 		if 'pdf' in t:
# 			try:
# 				[shutil.move(os.path.join('./'+f, t), os.path.join(os.getcwd(),t)) for t in tl]
# 			except IOError:
# 				pass

for f in os.listdir('.'):
	if 'pdf' in f and 'Papers' in f: os.rename(f, f.replace('Papers', ''))