#! /usr/bin/env python
# encoding:utf-8
import random

def Rochambeau(idea):
	dict_choice = {'stone':'1','shear':'2','paper':'3'}
	dict_result = {'11':'drew','22':'drew','33':'drew','12':'win','23':'win','31':'win','21':'lose','32':'lose','13':'lose'}
	pc_choice = random.choice(['stone','shear','paper'])
	print "pc choice : %s" % pc_choice
	return "the result is : %s" %dict_result[dict_choice[idea] + dict_choice[pc_choice]]



if __name__ == "__main__":
	while True:
		idea = raw_input("Please input your idea:stone or shear or paper(e to exit)\n")
		print '-'*30
		print("your choice :%s") %idea
		if idea.lower().strip() == 'e':
			break
		elif (idea != 'stone') and (idea != 'shear') and (idea !='paper'):
			print "please check your input"
			continue
		print(Rochambeau(idea))

