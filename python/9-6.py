#! /usr/bin/env python
#  encoding:utf-8
F1 = raw_input('please input a filename:')
F2 = raw_input('please input a filename:')
f1 = open(F1,'r')
f1alllines = f1.readlines()
f1.close()
f2 = open(F2,'r')
f2alllines = f2.readlines()
f2.close()

len1 = len(f1alllines)
len2 = len(f2alllines)

smallfile = len1 if len1 < len2 else len2
for i in range(smallfile):
	if cmp(f1alllines[i],f2alllines[i]) != 0:
		print 'row is %d' %(i+1)
		len3 = len(f1alllines[i])
		len4 = len(f2alllines[i])
		smallstr = len3 if len3 < len4 else len4
		for j in range(smallstr):
			if cmp(f1alllines[i][j],f2alllines[i][j]) != 0:
				print 'column is %d ' %(j+1)
				break
		break
else:
	if len1 == len2:
		print '2 files equal'
	else:
		print 'row is % d' %(i+2)
