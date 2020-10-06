import datetime
import calendar
import sys
import os
print("enter date: ")
(date,month,year) = sys.stdin.readline().split() 
x = datetime.datetime(int(year),int(month),int(date))
print(calendar.day_name[x.weekday()])