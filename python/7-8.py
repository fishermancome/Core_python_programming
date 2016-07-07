#! /usr/bin/env python
# encoding:utf-8

dict1 = {}
dict2 = {}

while True:
	name = raw_input("please input a worker name: ")
	if name == '--':
		break
	number = raw_input('please input a worker number:')
	dict1[name] = number
	dict2[number] = name

for key in sorted(dict1):
	print key,dict1[key]
print

for key in sorted(key):
	print key,dict2[key]
