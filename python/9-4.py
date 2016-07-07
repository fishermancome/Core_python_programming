#! /usr/bin/env python
#  encoding:utf-8
import os
filename = raw_input('please inputa filename:')
n = 0

f = open(filename,'r')

for i in f:
	print i,
	n += 1
	if n == 25:
		n = 0
		os.system('pause')
f.close()

