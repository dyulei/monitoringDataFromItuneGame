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
reload(sys)
sys.setdefaultencoding('utf8')
conn.set_character_set('utf8')
str_time = time.strftime('%Y-%m-%d %T', time.localtime(time.time()))
for i in range(1, 200):
	html = open('/Users/Levi/github/monitoringDataFromItuneGame/2014-07-31Paid/%d.html' % i , 'r')
	hjson = json.loads(html.read())

	print hjson['results'][0]['trackName']

	if(hjson['results'][0].has_key('averageUserRating') == False):
		hjson_averageUserRating = 0
		hjson_userRatingCount = 0

	else :
		hjson_averageUserRating = hjson['results'][0]['averageUserRating']
		hjson_userRatingCount = hjson['results'][0]['userRatingCount']



	t = ("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	values ('%d', '%s', '%s', 0, '%s', '%s', 'null', '%s', '%s', '%s', 'null', 'null', '%d', '%s', \
		'null', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%f', 0)" % (hjson['results'][0]['trackId'], conn.escape_string(hjson['results'][0]['trackName']), conn.escape_string(hjson['results'][0]['sellerName']) ,
		hjson['results'][0]['fileSizeBytes'], hjson['results'][0]['releaseDate'], conn.escape_string(hjson['results'][0]['description']), hjson['results'][0]['artworkUrl60'], hjson['results'][0]['trackViewUrl'], 
		hjson['results'][0]['artistId'], conn.escape_string(hjson['results'][0]['artistName']), hjson_averageUserRating, str_time, str_time, hjson_userRatingCount, hjson['results'][0]['bundleId'],hjson['results'][0]['version'], 
		hjson['results'][0]['currency'], hjson['results'][0]['price'] ))

	try: 
		cur.execute(t)
	except MySQLdb.IntegrityError, e:
		pass


	
conn.commit()
cur.close()
conn.close()



