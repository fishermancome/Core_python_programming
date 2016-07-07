#! /usr/bin/env python
#  encoding:utf-8

filename = raw_input('please input a filename:')
f = open(filename,'r')
alllines = f.readlines()
f.close()

print(len(alllines))
