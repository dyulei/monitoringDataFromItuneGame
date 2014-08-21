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
# create_time = '2014-01-18'


def saveDataBase(create_time, appType, appTypeNum):
	if os.path.exists('/Users/Levi/github/monitoringDataFromItuneGame/%s%s' % (create_time, appType)) == False:
		return 
	for i in range(1, 201):
		html = open('/Users/Levi/github/monitoringDataFromItuneGame/%s%s/%d.html' % (create_time,appType, i) , 'r')
		hjson = json.loads(html.read())
		# print i
		# print hjson['results'][0]['trackName']


		tb_version = ("insert into tb_version (app_id, version, created_at, updated_at) values ('%d', '%s','%s', '%s')" % (hjson['results'][0]['trackId'],hjson['results'][0]['version'],create_time, str_time))
		try: 
			cur.execute(tb_version)
		except MySQLdb.IntegrityError, e:
			pass
		conn.commit()


for i in range(10, 20):
	print i
	create_time = '2014-08-%02d' % i
	print 'Free'
	saveDataBase(create_time,'Free', 0)
	print 'Paid'
	saveDataBase(create_time,'Paid', 1)
	print 'Grossing'
	saveDataBase(create_time,'Grossing', 2)

# create_time = '2014-08-01'
# print 'Free'
# saveDataBase(create_time,'Free', 0)
# print 'Paid'
# saveDataBase(create_time,'Paid', 1)
# print 'Grossing'
# saveDataBase(create_time,'Grossing', 2)




# class myThread(threading.Thread):
# 	def __init__(self, url, kind):
# 		threading.Thread.__init__(self)
# 		self.url = url
# 		self.kind = kind

# 	def run(self):
# 		print 'kind : %s ' % self.kind
# 		download(self.url, self.kind)

# def test():
# 	thread1 = myThread('https://itunes.apple.com/cn/rss/topfreeapplications/limit=200/genre=6014/json', 'Free')
# 	thread2 = myThread('https://itunes.apple.com/cn/rss/toppaidapplications/limit=200/genre=6014/json', 'Paid')
# 	thread3 = myThread('https://itunes.apple.com/cn/rss/topgrossingapplications/limit=200/genre=6014/json', 'Grossing')
# 	thread1.start()
# 	thread2.start()
# 	thread3.start()
# 	thread1.join()
# 	thread2.join()
# 	thread3.join()


cur.close()
conn.close()



