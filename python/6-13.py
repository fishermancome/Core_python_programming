#! /usr/bin/env python
# encoding:utf-8

def atoc(string):
	flag_index = string.rfind('-')
	if flag_index <= 0:
		flag_index = string.rfind('+')
	if flag_index > 0:
		real = float(string[0:flag_index])
		imag = float(string[flag_index:-1])
	return complex(real,imag)

print atoc('-1.23e+4-5.67j')
