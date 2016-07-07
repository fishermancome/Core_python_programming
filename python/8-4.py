#! /usr/bin/env python
# encoding:utf-8

import math

def isprime(number):
	num = int(math.sqrt(number))
	while num > 1:
		if number % num == 0:
			return False
		num -= 1
	else:
		return True

print zip(range(1,12),(isprime(x)for x in range(1,12)))
