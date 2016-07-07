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
print A|B
print A&B


