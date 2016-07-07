#! /usr/bin/env python 
# encoding:utf-8

def MinToHour(min):
	hour = min/60
	mins = min-hour*60
        return hour,mins
if __name__ == "__main__":
	min = int(raw_input("请输入分钟数:\n"))
	print MinToHour(min)
