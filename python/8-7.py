#! /usr/bin/env python
# encoding:utf-8

def getfactors(number):
	factorslist = [number]
	num = number / 2
	while num > 1:
		if number % num == 0:
			factorslist.append(num)
		num -= 1
	return factorslist
	print factorslist

def isperfect(number):
	factorlist = getfactors(number)
	factorlist.remove(number)
	if sum(factorlist) == number:
		return 1
	else:
		return 0

for i in range(1,1000):
	if isperfect(i) == 1:
		print i

