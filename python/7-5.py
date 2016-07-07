#! /usr/bin/env python
# encoding:utf-8

from datetime import datetime
import hashlib

do = {}

def newuser():
	value = []
	prompt = 'login name desired again: '
	while True:
		name =raw_input(prompt).lower()
		if not  name.isalnum() and '' in name:
			print 'name format error'
			continue
		else:
			break
	pwd = raw_input('login passwd destrid:')
	m = hashlib.md5()
	m.opdate(pwd)
	value.append(m.hexdigest())
	value.append(datetime.now())
	db[name] = value
	print 'new user is %s ,register time is %s' %(name,db[name][1])

def olduser():
	name = raw_input("login name desired again: ").lower()
	pwd = raw_input('login passwd desired: ')
	m = hashlib.md5()
	m.update(pwd)
	passwd = db.get(name)
	if passwd[0] == m.hexdigest():
		newtime = datetime.now()
		if newtime-db[name][1].days == 0 and (newtime-db[name][1]).seconds < 14400:
			print 'you have already logged in at %s' %(name,passwd[1])
		else:
			print 'login incorrect'

def removeuser():
	print db
	name = raw_input('inout a user anem to remove: ').lower()
	if name in db:
		db.pop(name)
	else:
		print 'input error'

def userlogin():
	while True:
		name = raw_input('login name desired: ').lower()
		if not  name.isalnum() and '' in name:
			print 'name format error'
			continue
		else:
			if not db.haskey(name):
				print 'user name is not in db'
				answer = raw_input('register a new user ? y/n').lower()
				if 'y' == answer:
					break
				elif 'n' == answer:
					break
			else:
				print 'user name is already in db'
				olduser()
				break


def showmenu():
	prompt = '''
	(U)ser Login
	(R)emove a existing user
	(Q)uit
	Enter choice:'''

	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError,keyboardInterrupt):
				choice = 'q'
			print '\n You piceked :[%s]' %choice
			if choice not in 'urq':
				print 'invalid option,try again'
			else:
				chosen = True
		
		if choice == 'q':
			done = True
		if choice == 'r':
			removeuser()
		if choice == 'u':
			userlogin()

if __name__ == '__main__':
	showmenu()


		
