#! /usr/bin/env python
# encoding:utf-8

def merge(list1,list2):
	return dict(zip(list1,list2))


if __name__ == "__main__":
	list1 = [1,2,3]
	list2 = ['abc','def','ghi']
	print merge(list1,list2)

