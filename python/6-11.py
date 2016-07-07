#! /usr/bin/env python
# encoding:utf-8


def format_ip():
	num  = raw_input("please input ip(12 integer):\n")
	x = num[0:3]
	y = num[3:6]
	z = num[6:9]
	q = num[9:12]
	temp = [x,y,z,q]
	ip = '.'.join(temp)
	return ip

if __name__ == "__main__":
	print format_ip()

print '------------------------(b)------------------------------'
def re_format_ip():
	ip = raw_input("Enter ip:\n")
	temp = ip.split('.')
	num =''.join(temp)
	return num


if __name__ =="__main__":
	print re_format_ip()


