#! /usr/bin/env python
# encoding:utf-8

import types
#(a)
def findchr(string,char):
	print "the string is %s,the char is %s" %(string,char)
	result = []
	for i ,j in enumerate(string):
		if char == j:
			result.append(i)
	if len(result) != 0:
		print "the index of  char:"
		return result
	else:
		return -1
		
print (findchr("yesterday once more",'o'))

#(b)

def rfindchr(string,char):
	print "the string is %s,the char is %s" %(string,char)
	l = len(string)
	for i,j in enumerate(string[::-1]):
		if char == j:
			result = l-i
			break
	if type(result) is types.IntType:
		print "the last index of char:"
		return result
	else:
		return -1

print (rfindchr("yesterday once more",'o'))



#(c)

def subchr(string,origchar,newchar):
	print "the string is %s,the origchar is %s,the newchar is %s" %(string,origchar,newchar)
	result = []
	str_list = list(string)
	for i,j in enumerate(str_list):
		if origchar == j:
			str_list[i]= newchar
	result = ''.join(str_list)
	return result

print (subchr("yesterday once more","once more","is beautiful"))
	
