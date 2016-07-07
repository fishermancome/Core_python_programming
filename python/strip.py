#! /usr/bin/env python
# encoding:utf-8

original =raw_input("ENter a string:\n")
length = len(original)
print length

for i in range(0,length):
	if original[i]<>' ':
		lstrip=original[i:]
		print len(lstrip)
		break
	else:
		pass

for i in range(1,length+1):
	if lstrip[-1]<>' ':
		strip=lstrip
		break
	elif lstrip[-i]<>' ':
		strip=lstrip[:-i+1]
		print len(strip)
		break
	else:
		pass


print strip




 
