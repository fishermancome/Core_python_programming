#! /usr/bin/env python
# coding:utf-8

def blank():
	get_str=raw_input("please input your string:\n")
	r = len(get_str)-1
	l = 0
	while get_str[l] == ' ':
		l += 1
	while get_str[r] == ' ':
		r -= 1
	result = get_str[l:r+1]
	return result

if __name__=='__main__':
	print blank()

