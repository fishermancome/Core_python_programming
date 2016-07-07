#! /usr/bin/env python
# encoding:utf-8

def getfibonacci(number):
	if number == 1 or number == 2:
		return 1
	else:
		befornumbers =[1,1]
		for i in range(3,number):
			fibonacci = sum(befornumbers)
			befornumbers.pop(0)
			befornumbers.append(fibonacci)
		else:
			return sum(befornumbers)


print getfibonacci(6)	
