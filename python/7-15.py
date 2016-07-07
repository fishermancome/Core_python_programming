#! /usr/bin/env python
# encoding:utf-8

tmp_1 = eval(raw_input("please input set A,separate by comma:"))
tmp_2 = eval(raw_input("please input set B,separate by comma:"))

A = set(tmp_1)
B = set(tmp_2)


print A
print B


while True:
	op  = raw_input("please choose a operator from (in,not in,&,|,^,<,<=,>,>=,==,!=)for A operator B:")
	if 'in' == op:
		print 'A in B is: ',A in B
	elif 'not in' ==op:
		print 'A not in B is: ',A not in B
	elif '&' == op:
		print 'A & B is: '.A & B
	elif '|' ==op:
		print 'A | B is: ',A | B
	elif '^' == op:
		print 'A ^ B is: '.A ^ B
	elif '<' ==op:            
		print 'A < B is: ',A < B
	elif '<=' == op:                 
       		print 'A <= B is: ',A <= B	
	elif '>' ==op:
                print 'A > B is: ',A > B
       	elif '>=' == op:
            	print 'A >= B is: ',A >= B
	elif '==' == op:
		print 'A == B is: ',A == B
	elif '!=' == op:
		print 'A != B is: ',A != B
	else:
		print 'input error'
		break
