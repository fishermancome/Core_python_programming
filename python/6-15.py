#! /usr/bin/env python
# encoding:utf-8
import time
from datetime import date

def calcdate(string1,string2):
	temp_list1 = string1.split('/')
	temp_list2 = string2.split('/')
	days_count = ""
	first_date = date(int(temp_list1[2]),int(temp_list1[1]),int(temp_list1[0]))
	second_date = date(int(temp_list2[2]),int(temp_list2[1]),int(temp_list2[0]))
	if first_date < second_date:
		date_count = abs(second_date - first_date)
	return days_count.days


def calcbirth(string):
	today = date.today()
	time_to_birth = ""
	time_list = string.split('/')
	birth = date(int(temp_list[2]),int(temp_list[1]),int(temp_list[0]))
	if birth < today:
		time_to_birth = abs(today - birth)
	else:
		print("please input the right birth")
	return time_to_birth.days

def nextbirth(string):
	today = date.today()
	time_to_birth = ""
	temp_list = string.split('/')
	month_day = date(today.year,int(temp_lsit[1]),int(temp_list[0]))
	birth = date(int(today.year + 1),int(temp_list[1]),int(temp_list[0]))
	if today < month_day:
		next_time_to_birth = abs(month_day-today)
	elif today < birth:
		next_time_to_birth = abs(birth - today)
	else:
		print("Please input the right birth")
	return next_time_to_birth.days


if __name__ == "__main__":
	while True:
		choice = raw_input("I can do something:\na: Count the number of days between two date\n"
"b:Count the number of days since you born\n"
"c:Count the number of days before your next birth\n"
"q to exit\n")
		if choice == 'q':
			break
		elif choice == 'a':
			str_1 = raw_input("Please enter your first date:like DD/MM/YY \n")
			str_2 = raw_input("Please enter your second date\n")
			try:
				print("The number of gays between two date is ",calcdate(str_1,str_2))
			except:
				print("Please check your enter format DD/MM/YY")
		elif choice == 'b':
			str_date = raw_input("Please enter your date:like DD/MM/YY \n")
			try:
				print "You had born" ,calcbirth(str_date),"days"
			except:
				print("Please check your enter format DD/MM/YY")
		elif choice == 'c':
			str_date = raw_input("Please enter your birth date:like DD/MM/YY\n")
			try:
				print "There are",nextbirth(str_date),"days of your next birthdays"
			except:
				print("Please check your enter format DD/MM/YY")
