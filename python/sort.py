#! /usr/bin/env python
astring = raw_input("Enter a list of num:")
alist = astring.split()
print alist

ilist=[]
for s in alist:
	i = int(s)
	ilist.append(i)

print ilist
print sorted(ilist)
print sorted(alist)
