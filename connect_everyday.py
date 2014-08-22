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



def saveDataBase(create_time, appType, appTypeNum):
	if os.path.exists('/Users/Levi/github/monitoringDataFromItuneGame/%s%s' % (create_time, appType)) == False:
		return 
	for i in range(1, 201):
		html = open('/Users/Levi/github/monitoringDataFromItuneGame/%s%s/%d.html' % (create_time,appType, i) , 'r')
		hjson = json.loads(html.read())
		print i
		print hjson['results'][0]['trackName']


		if(hjson['results'][0].has_key('averageUserRating') == False):
			hjson_averageUserRating = 0
		else :
			hjson_averageUserRating = hjson['results'][0]['averageUserRating']


		if(hjson['results'][0].has_key('userRatingCount') == False):
			hjson_userRatingCount = 0
		else :
			hjson_userRatingCount = hjson['results'][0]['userRatingCount']


		if(hjson['results'][0].has_key('userRatingCountForCurrentVersion') == True):
			hjson_userRatingCount = hjson['results'][0]['userRatingCountForCurrentVersion']



		tb_app = ("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
		filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
		values ('%d', '%s', '%s', 0, '%s', '%s', 'null', '%s', '%s', '%s', 'null', 'null', '%d', '%s', \
			'null', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%f', 0)" % (hjson['results'][0]['trackId'], conn.escape_string(hjson['results'][0]['trackName']), conn.escape_string(hjson['results'][0]['sellerName']) ,
			hjson['results'][0]['fileSizeBytes'], hjson['results'][0]['releaseDate'], conn.escape_string(hjson['results'][0]['description'].encode("utf8","ignore")), hjson['results'][0]['artworkUrl60'], hjson['results'][0]['trackViewUrl'], 
			hjson['results'][0]['artistId'], conn.escape_string(hjson['results'][0]['artistName']), hjson_averageUserRating, create_time, str_time, hjson_userRatingCount, hjson['results'][0]['bundleId'],hjson['results'][0]['version'], 
			hjson['results'][0]['currency'], hjson['results'][0]['price'] ))

		tb_rank = ("insert into tb_rank (app_id, rank_type, rank, created_at, updated_at) values ('%d', '%d', '%d','%s', '%s')" % (hjson['results'][0]['trackId'], appTypeNum,i,create_time, str_time))


		if(hjson['results'][0].has_key('sellerUrl') == False):
			hjson_sellerUrl = 'null'
		else :
			hjson_sellerUrl = conn.escape_string(hjson['results'][0]['sellerUrl'])

		tb_company = ("insert into tb_company (artistId, artistName, sellerUrl, created_at, updated_at) values ('%d', '%s', '%s','%s', '%s')" % (hjson['results'][0]['artistId'], conn.escape_string(hjson['results'][0]['artistName']), \
			hjson_sellerUrl,create_time, str_time))


		tb_version = ("insert into tb_version (app_id, version, created_at, updated_at) values ('%d', '%s','%s', '%s')" % (hjson['results'][0]['trackId'],hjson['results'][0]['version'],create_time, str_time))



		genres_count = 0
		for genres_string in hjson['results'][0]['genres']:
			genres_count+=1


		for genres_id in range(0, genres_count):
			# print hjson['results'][0]['genres'][genres_id]
			# print hjson['results'][0]['genreIds'][genres_id]
			tb_category = ("insert into tb_category (category_id, category_name, created_at, updated_at) values ('%d', '%s','%s', '%s')" % (int(hjson['results'][0]['genreIds'][genres_id]), hjson['results'][0]['genres'][genres_id], \
			create_time, str_time))

			tb_app_category = ("insert into tb_app_category (app_id, category_id, created_at, updated_at) values ('%d', '%d','%s', '%s')" % (hjson['results'][0]['trackId'], int(hjson['results'][0]['genreIds'][genres_id]), \
			create_time, str_time))

			try: 
				cur.execute(tb_category)
			except MySQLdb.IntegrityError, e:
				pass

			try: 
				cur.execute(tb_app_category)
			except MySQLdb.IntegrityError, e:
				pass

		try: 
			cur.execute(tb_version)
		except MySQLdb.IntegrityError, e:
			pass

		cur.execute(tb_rank)
		try: 
			cur.execute(tb_app)
		except MySQLdb.IntegrityError, e:
			pass

		try: 
			cur.execute(tb_company)
		except MySQLdb.IntegrityError, e:
			pass


# for i in range(3, 18):
# 	print range
# 	create_time = '2014-08-%02d' % i
# 	print 'Free'
# 	saveDataBase(create_time,'Free', 0)
# 	print 'Paid'
# 	saveDataBase(create_time,'Paid', 1)
# 	print 'Grossing'
# 	saveDataBase(create_time,'Grossing', 2)

create_time = str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print create_time
print 'Free'
saveDataBase(create_time,'Free', 0)
print 'Paid'
saveDataBase(create_time,'Paid', 1)
print 'Grossing'
saveDataBase(create_time,'Grossing', 2)
conn.commit()




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



