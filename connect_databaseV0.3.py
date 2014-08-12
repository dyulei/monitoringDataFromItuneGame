#!/usr/bin/python
# coding: utf-8
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
conn.set_character_set('utf8')
str_time = time.strftime('%Y-%m-%d %T', time.localtime(time.time()))
for i in range(1, 5):
	html = open('/Users/Levi/github/monitoringDataFromItuneGame/14.7.30Paid/%d.html' % i , 'r')
	hjson = json.loads(html.read())

	# cur.execute("insert into tb_app (app_id, app_name, author, fit_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	# filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price) \
	# values ('100', 'adf', 'Tencent', 'iphone4', '9500', '2013-02-04', 'null', 'null', 'null', 'null', 'null', 'null', '12345', 'Tencent', \
	# 	'NULL', '5', '2014-03-02', '2011-03-01', '12', '1234567', '4.0', '3', '12')")

	# cur.execute("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	# filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	# values ('20', 'app_name', 'author', '0', '4567', '2011-11-11', 'rom_type', 'description', 'icon_Url', 'trackViewUrl', 'download_url', 'filename', '1234356', 'company_name', \
	# 	'filemd5', '12', '2011-11-11', '2011-11-11', '23456', 'bundleId','version', 'currency', '12', '10')")

	# cur.execute("insert into tb_test (id, str, date) values ('%d', 'null', '%s')" %  (hjson['results'][0]['trackId'], str_time) )
	print hjson['results'][0]['trackName']
	print hjson['results'][0]['price']
	print hjson['results'][0]['averageUserRating']
	if(hjson)
	# cur.execute("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	# filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	# values ('%d', '%s', '%s', 0, '%s', '%s', 'null', '%s', '%s', '%s', 'null', 'null', '%d', '%s', \
	# 	'null', '%d', '%s', '%s', '%d', 'null' ,'%s', '%s', '%f', 0)" % (hjson['results'][0]['trackId'], hjson['results'][0]['trackName'], hjson['results'][0]['sellerName'] ,
	# 	hjson['results'][0]['fileSizeBytes'], hjson['results'][0]['releaseDate'], hjson['results'][0]['description'], hjson['results'][0]['artworkUrl60'], hjson['results'][0]['trackViewUrl'], 
	# 	hjson['results'][0]['artistId'], hjson['results'][0]['artistName'], hjson['results'][0]['averageUserRating'], str_time, str_time, hjson['results'][0]['userRatingCount'], hjson['results'][0]['version'], 
	# 	hjson['results'][0]['currency'], hjson['results'][0]['price'] ))

	

	cur.execute("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	values ('%d', '%s', '%s', 0, '%s', '%s', 'null', '%s', '%s', '%s', 'null', 'null', '%d', '%s', \
		'null', '%d', '%s', '%s', '%d', 'null', '%s', '%s', '%f', 0)" % (hjson['results'][0]['trackId'], hjson['results'][0]['trackName'], hjson['results'][0]['sellerName'] ,
		hjson['results'][0]['fileSizeBytes'], hjson['results'][0]['releaseDate'], hjson['results'][0]['description'], hjson['results'][0]['artworkUrl60'], hjson['results'][0]['trackViewUrl'], 
		hjson['results'][0]['artistId'], hjson['results'][0]['artistName'], hjson['results'][0]['averageUserRating'], str_time, str_time, hjson['results'][0]['userRatingCount'], hjson['results'][0]['version'], 
		hjson['results'][0]['currency'], hjson['results'][0]['price'] ))


	# cur.execute("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url,filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	# values (112323, 'app_name', 'author', 0, 'size', '2011-11-11', 'rom_type', 'description', 'icon_Url', 'trackViewUrl', 'download_url', 'filename', 123456, 'company_name', \
	# 	'filemd5', 12, '2011-11-11', '2011-11-11', 23456, 'bundleId' ,'version', 'currency', 12, 10)")



	
conn.commit()
cur.close()
conn.close()



