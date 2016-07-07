#! /usr/bin/env python
# encoding:utf-8


import string
upperdict = {}
lowerdict = {}
upperletters = string.uppercase
lowerletters = string.lowercase
dststr = []
oristr = raw_input("Enter a string to rot13:")
print 'Your string to en/coypt was: ',oristr

for i in range(0,len(lowerletters)):
	if i < 13:
		lowerdict[lowerletters[i]] = lowerletters[i+13]
	else:
		lowerdict[lowerletters[i]] = lowerletters[i-13]

for i in range(0,len(upperletters)):
	if i < 13:
		upperdict[upperletters[i]] = upperletters[i+13]
	else:
		upperdict[upperletters[i]] = upperletters[i-13]

for ch in oristr:
	if ch in lowerdict:
		dststr.append(lowerdict[ch])
	elif ch in upperdict:
		dststr.append(upperdict[ch])
	else:
		dststr.append(ch)
dststr=''.join(dststr)

print 'the rot13 string is :',dststr
