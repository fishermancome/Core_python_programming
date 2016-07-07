#! /usr/bin/env python
# encoding:utf-8
import sys
dict1 = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":""}
dict2 = {"1":"ten","2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety","0":""}
dict3 = {"1":"one hundred","2":"two hundred","3":"three hundred","4":"four hundred","5":"five hundred","6":"six hundred","7":"seven hundred","8":"eight hundred","9":"nine hundred","0":""}

dictAll = {1:dict1,2:dict2,3:dict3}

def fun(str_num):
	if int(str_num) > 1000 or int(str_num) < 0:
		return "Invalid NUmber,Please input again"
	length = len(str_num)
	str_temp = ""
	if len(str_num) == 4:
		str_temp = "One Thousand"
		return str_temp
	for i in range(length):
		str_temp += dictAll[length - i][str_num[i]]+""
	return str_temp

if __name__ == "__main__":
	while True:
		str_num =raw_input("please  input a number, exit with 'q':\n")
		if str_num == 'q':
			sys.exit()
		else:
			print fun(str_num)
