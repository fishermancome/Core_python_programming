#! /usr/bin/env pyhton
# encoding:utf-8

namelist = []
count = 0

while True:
	name = raw_input("please enter the name like(last name,first name)(exit with q)")
	if name.lower() == 'q':
		for item in namelist:
			print item
			break
	if name.find(',') == -1:
		count += 1
		print 'wrong time %d' %count
		namelist.append([name.split(" ")])
	else:
		namelist.append([name.split(",")])
