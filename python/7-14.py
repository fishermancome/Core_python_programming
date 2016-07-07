#! /usr/bin/env python
# encoding:utf-8


import random

tmp = []
for i in range(0,10):
	tmp.append(random.randint(0,9))
A = set(tmp)
tmp = []

for i in range(0,10):
	tmp.append(random.randrange(0,10))
B = set(tmp)

print A
print B

tmpanswer_1 = []
answer_1 = []

for i in range(0,3):
	tmpanswer_1 = raw_input("please input answer for A|B,seprate by comma: ").split(',')
	for j in tmpanswer_1:
		answer_1.append(int(j))
	C = set(answer_1)	
	if C == (A|B):
		print 'you are right'
		break
	elif 2 == i:
		print 'the answer of A|B is: ',A|B
	else:
		print 'you are wrong'                                                                                                                         

tmpanswer_2 = []
answer_2 = []

for i in range(0,3):
	tmpanswer_2 = raw_input("please input answer for A&B,seprate by comma: ").split(',')
	for j in tmpanswer_2:
		answer_2.append(int(j))
	C = set(answer_2)	
	if C == (A&B):
		print 'you are right'
		break
	elif 2 == i:
		print 'the answer of A&B is: ',A&B
	else:
		print 'you are wrong'                   



tmp = []
for i in range(0,10):
	tmp.append(random.randint(0,9))
D = set(tmp)

tmp = []
for i in range(0,6):
	tmp.append(random.randint(1,9))
E =set(tmp)


print 'set D is ',D
print 'set E is ',E

for i in range(0,2):
	tmpanswer_3 = raw_input('set E is subset of set D,y/n?')
	if 'y' == tmpanswer_3:
		if E.issubset(D):
			print 'you are right'
			break
		elif 1 == i:
			print 'the subset of D is' ,D.intersection(E) 
		else:
			print 'you are wrong'
	elif 'n' == tmpanswer_3:
		if E.issubset(D):
			print"you are wrong"
		elif 1 == i:
			print 'the subset of D is',D.intersection(E)
		else:
			print 'you are right'
			break
	else:
		print'input error,only y/n valid'
