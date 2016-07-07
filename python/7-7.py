#! /usr/bin/env python
# encoding:utf-8

idict = {1:'a',2:'b',3:'c'}

def change_dict(tdict):
	mydict = {}
	for key in tdict:
		mydict.update({}.fromkeys(tdict[key],key))
	print mydict

change_dict(idict)
