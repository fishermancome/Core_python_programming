#! /usr/bin/env python
# encoding:utf-8

def transfer(string):
	temp_str=string.swapcase()
	return temp_str
if __name__ == "__main__":
	while True:
		string = raw_input("please input a string:\n")
		if string == 'q':
			break
		print transfer(string)
	


