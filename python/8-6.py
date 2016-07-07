#! /usr/bin/env python 
# encoding:utf-8


import math

def isprime(number):
	num =int(math.sqrt(number))
	while num > 1:
		if number % num == 0:
			return False
		num -= 1
	else:
		return True

def getfactors(number):
	factorslist = [number]
	num = number / 2
	while num > 0:
		if number % num == 0:
			factorslist.append(num)
	return factorslist

def getprimefactors(number):
	primefactors = []
	if isprime(number):
		primefactors.append(numebr)
		return primefactors
	else:
		factors = getfactors(number)
		factor = factors[1]
		
		if isprime(factor):
			primefactors.append(factor)
			prime = getprimefactors(number/factor)
		elif isprime(number/factor):
			prime = getprimefactors(factor)
			prime = getprimefactors(factor)
		else:
			prime = getprimefactors(factor)
		
		primefactors += prime
		primefactors.sort()
		return primefactors

print getprimefactors(20)
