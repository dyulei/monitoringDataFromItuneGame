#!/usr/bin/env python
#-*- coding:utf-8 -*-
import MySQLdb
import time
import sys, string, os
import urllib
import re
import json
import urllib2

conn = MySQLdb.connect(host="121.201.10.15",
		user='eagleeye',
		passwd='EYeapp$ea@2',
		db="db_rankapp",
		port=30013)

cur = conn.cursor()
reload(sys)
sys.setdefaultencoding('utf8')
conn.set_character_set('utf8')




tb_app = ("select * from tb_app ")
total = int(cur.execute(tb_app))

tb_rank_orderby_releasetime = ("SELECT t.app_name, t.icon_Url, t.release_date FROM db_rankapp.tb_app t where release_date like '%2009-10-23%' order by release_date;")
cur.execute(tb_rank_orderby_releasetime)
recs = cur.fetchall()
for rank in recs:
	print rank[2]


gamelist = []
data = {"status": 0, "message": '', "data": {"total": total, "list": gamelist}}

t = {'dd': 12}
# print data


conn.commit()
cur.close()
conn.close()