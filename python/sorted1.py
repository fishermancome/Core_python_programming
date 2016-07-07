#! /usr/bin/env python
# coding:utf-8
def get_num():
	global num_list
	num_list = []
	num= ''
	while num != '!':
		num = raw_input('输入一些数字 以！结束').strip()
		if num != '!':
			try:
				num = float(num)
			except:
				print '输入有误，请重新输入'
				get_num()
			else:
				num_list.append(num)
		else:
			break
	return num_list
def sort_descending():
	get_num()
	print sorted(num_list,reverse = True)

print('--------------(a)------------')
sort_descending()
