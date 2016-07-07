#! /usr/bin/env python
# encoding:utf-8

dicta = dict(b=2,a=1,c=3)
for key in sorted(dicta):
	print key

dicta = dict(b=2,a=1,c=3)
for key in sorted(dicta):
	print 'key=%s,value=%s' %(key,dicta[key])

dicta = {2:'b',1:'a',3:'c'}
listvalue = dicta.values()
listvalue.sort()
for value in listvalue:
	for key in dicta.keys():
		if value == dicta[key]:
			print 'key = %s,value = %s' %(key,dicta[key])
