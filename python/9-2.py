#! /usr/bin/env python
# encoding:utf-8

N = int(raw_input('please input a number:'))
F = raw_input('please input a filename:')

f = open(F,'r')
alllines = f.readlines()
f.close()

for i in range(N):
	print alllines[i],
