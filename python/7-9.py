#! /usr/bin/env python
# encoding:utf-8

srcstr1 = 'abc'
dststr1 = 'mno'
string1 = 'Abcdef'
srcstr2 = 'abcDef'
dststr2 = 'mno'
string2 = 'Abcdefghi'

def tr(srcstr,dststr,string,case=0):
	mylist = []
	if 0 == case:
		dicta = dict(zip(srcstr.lower(),dststr))
		if len(srcstr) > len(dststr):
			dicta.update({}.fromkeys(srcstr[len(dststr):]))
		for ch in string.lower():
			if ch in dicta:
				mylist.append(dicta[ch])
			else:
				mylist.append(ch)
		else:
			dicta = dict(zip(srcstr,dststr))
			if len(srcstr) >len(dststr):
				dicta.update({}.fromkeys(srcstr[len(dststr):]))
			for ch in string:
				if ch in dicta:
					mylist.append(dicta[ch])
				else:
					mylist.append(ch)
		mylist = [ch for ch in mylist if ch]
		print ''.join(mylist)

tr(srcstr1,dststr1,string1,0)
tr(srcstr2,dststr2,string2,0)

