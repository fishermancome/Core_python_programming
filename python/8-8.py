#! /usr/bin/env python
# encoding:utf-8

def getfactorial(number):
	product = 1
	for i in range(2,number+1):
		product *= i
	else:
		return product

print(getfactorial(10))
