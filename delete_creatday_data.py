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



def deleteDataBase(create_time):


	tb_app = ("delete from db_rankapp.tb_app where created_at like '%s%%' " % create_time)


	tb_app_category = ("delete from db_rankapp.tb_app_category where created_at like '%s%%' " % create_time)

	tb_company = ("delete from db_rankapp.tb_company  where created_at like '%s%%' " % create_time)


	tb_rank = ("delete from db_rankapp.tb_rank  where created_at like '%s%%' " % create_time)

	tb_version = ("delete from db_rankapp.tb_version where created_at like '%s%%' " % create_time)


	cur.execute(tb_app)
	cur.execute(tb_app_category)
	cur.execute(tb_company)
	cur.execute(tb_rank)
	cur.execute(tb_version)



create_time = str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print create_time
deleteDataBase(create_time)
conn.commit()



cur.close()
conn.close()



