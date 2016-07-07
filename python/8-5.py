#! /usr/bin/env python
# encoding:utf-8

def getfactors(number):
	factorslist = [number]
	num = number / 2
	while num > 0:
		if number % num == 0:
			factorslist.append(num)
		num -=1
	
	return factorslist

print getfactors(124)
