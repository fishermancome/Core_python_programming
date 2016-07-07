#! /usr/bin/env python
# encoding:utf-8

def get():
	global get_num
	get_num =raw_input("pleae input your number:\n")
	try:
		get_num =int(get_num)
	except:
		print("Error Input,please input a number!")
		get()
	else:
		print("Input Success!")


eng_list = []
eng = "zero,one,two,three,four,five,six,seven,eight,nine"
eng_list=eng.split(',')
result = []
get()
get_list = list(str(get_num))
for i in get_list:
	result.append(eng_list[int(i)])
print '-'.join(result)

print '-----------------附加题-------------------'
str1 = "zero,one,two,three,four,five,six,seven,eight,nine"
str2 = "ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen"
str3 = "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety"

eng1 = []
eng2 = []
eng3 = []
eng1 = str1.split(',')
eng2 = str2.split(',')
eng3 = str3.split(',')

get()


kilo = get_num / 1000
hund = get_num % 1000 / 100
deca = get_num % 100 / 10
unit = get_num % 10

if kilo != 0:
	if hund != 0:
		if int(deca) >= 2 and unit != 0:
			print eng1[int(kilo)],'thousand','-',eng1[int(hund)],'hundred','-',eng3[int(deca)-2],'-',eng1[int(unit)]
		elif int(deca) >= 2 and unit == 0:
			print eng1[int(kilo)],'thousand','-',eng1[int(hund)],'hundred','-',eng3[int(deca)-2]
		elif 1 <= int(deca) < 2:
			print eng1[int(kilo)],'thousand','-',eng1[int(hund)],'hundred','-',eng2[int(unit)]
		elif int(deca) == 0 and unit != 0:
			print eng1[int(kilo)],'thousand','-',eng1[int(hund)],'hundred','-',eng1[int(unit)]
		elif int(deca) == 0 and unit == 0:
			print eng1[int(kilo)],'thousand','-',eng1[int(hund)],'hundred'
	elif hund == 0:
		if int(deca) >= 2 and unit != 0:
			print eng1[int(kilo)],'thousand','-',eng3[int(deca)-2],'-',eng1[int(unit)]
		elif int(deca) >= 2 and unit == 0:
			print eng1[int(kilo)],'thousand','-',eng3[int(deca)-2]
		elif 1 <= int(deca) < 2:
			print eng1[int(kilo)],'thousand','-',eng2[int(unit)]
		elif int(deca) == 0 and unit != 0:
			print eng1[int(kilo)],'thousand','-',eng1[int(unit)]
		elif int(deca) == 0 and unit != 0:
			print eng1[int(kilo)],'thousand'
elif kilo == 0:
	if hund != 0:
		if int(deca) >= 2 and unit != 0:
			print eng1[int(hund)],'hundred','-',eng3[int(deca)-2],'-',eng1[int(unit)]
		elif int(deca) >= 2 and unit == 0:
			print eng1[int(hund)],'hundred','-',eng3[int(deca)-2]
		elif 1 <= int(deca) < 2 and unit != 0:
			print eng1[int(hund)],'hundred','-',eng2[int(unit)]
		elif int(deca) == 0 and unit != 0:
			print eng1[int(hund)],'hundred','-',eng1[int(unit)]
		elif int(deca) == 0 and unit == 0:
			print eng1[int(hund)],'hundred'
	elif hund == 0:
		if int(deca) >= 2 and unit != 0:
			print eng3[int(deca)-2],'-',eng1[int(unit)]
		elif int(deca) >= 2 and unit == 0:
			print eng3[int(deca)-2]
		elif 1 <= int(deca) < 2:
			print eng2[int(unit)]
		elif int(deca) == 0:
			print eng1[int(unit)] 

