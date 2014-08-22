#!/usr/bin/python
# coding: utf-8
import time
import datetime


str_time = time.strftime('%Y-%m-%d %T', time.localtime(time.time()))
print str_time
d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
print d1

d2 = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print d2


dd_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
d3 = datetime.datetime.strptime(dd_time, '%Y-%m-%d')
print d3

delta = d2 - d1 
print delta
print delta.days

delta = datetime.timedelta(days = 1)
print delta

d4 = d3 + delta
print d4