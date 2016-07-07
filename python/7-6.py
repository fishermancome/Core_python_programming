#! /usr/bin/env python
# encoding:utf-8

tlist = []
idict = {}

while True:
	mark = raw_input('pls input a stock mark: ')
	if mark == '--':
		break
	stock = raw_input('pls input a stock name: ')
	price = raw_input('pls input a stock price:')
	current = raw_input('pls input a stock current price:')
	print
	tlist.append([mark,stock,price,current])

print '0 mark'
print '1 stock'
while True:
	num = int(raw_input('pls input a key to sort:'))
	if num == 0:
		for i in range(0,len(tlist)):
			idict.update({}.fromkeys(tlist[i][0],tlist[i]))
		for eachkey in sorted(idict):
			print 'idict key ',eachkey,'has value',idict[eachkey]
		break
	elif num == 1:
		for i in range(0,len(tlist)):	
			idict.update({}.fromkeys(tlist[i][1],tlist[i]))
		for eachkey in sorted(idcit):
			print 'idict key',eachkey,'has value',idict[eachkey]	
		break
	else:
		print'input key wrong'
	continue
