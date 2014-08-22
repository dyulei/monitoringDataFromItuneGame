#!/usr/bin/python
# coding: utf-8
import MySQLdb
import time
import sys, string, os
import urllib
import re
import json
import urllib2
import threading

conn = MySQLdb.connect(host="121.201.10.15",
		user='eagleeye',
		passwd='EYeapp$ea@2',
		db="db_rankapp",
		port=30013)

cur = conn.cursor()
reload(sys)
sys.setdefaultencoding('utf8')
conn.set_character_set('utf8')

str_time = time.strftime('%Y-%m-%d %T', time.localtime(time.time()))


create_time = '2014-08-22'

tb_app = ("select * from db_rankapp.tb_rank t where t.created_at like '%s%%'" % create_time)
print tb_app