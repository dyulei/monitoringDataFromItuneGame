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
for i in range(1, 201):
	html = open('/Users/Levi/github/monitoringDataFromItuneGame/2014-08-19Free/%d.html' % i , 'r')
	hjson = json.loads(html.read())
	print i
	print hjson['results'][0]['trackName']


	if(hjson['results'][0].has_key('averageUserRating') == False):
		hjson_averageUserRating = 0
		hjson_userRatingCount = 0

	else :
		hjson_averageUserRating = hjson['results'][0]['averageUserRating']
		hjson_userRatingCount = hjson['results'][0]['userRatingCount']

	tb_app = ("insert into tb_app (app_id, app_name, author, app_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, \
	filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price, channel_id) \
	values ('%d', '%s', '%s', 0, '%s', '%s', 'null', '%s', '%s', '%s', 'null', 'null', '%d', '%s', \
		'null', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%f', 0)" % (hjson['results'][0]['trackId'], conn.escape_string(hjson['results'][0]['trackName']), conn.escape_string(hjson['results'][0]['sellerName']) ,
		hjson['results'][0]['fileSizeBytes'], hjson['results'][0]['releaseDate'], conn.escape_string(hjson['results'][0]['description'].encode("utf8","ignore")), hjson['results'][0]['artworkUrl60'], hjson['results'][0]['trackViewUrl'], 
		hjson['results'][0]['artistId'], conn.escape_string(hjson['results'][0]['artistName']), hjson_averageUserRating, str_time, str_time, hjson_userRatingCount, hjson['results'][0]['bundleId'],hjson['results'][0]['version'], 
		hjson['results'][0]['currency'], hjson['results'][0]['price'] ))

	tb_rank = ("insert into tb_rank (app_id, rank_type, rank, created_at, updated_at) values ('%d', '1', '%d','%s', '%s')" % (hjson['results'][0]['trackId'], i,str_time, str_time))


	if(hjson['results'][0].has_key('sellerUrl') == False):
		hjson_sellerUrl = 'null'
	else :
		hjson_sellerUrl = conn.escape_string(hjson['results'][0]['sellerUrl'])

	tb_company = ("insert into tb_company (artistId, artistName, sellerUrl, created_at, updated_at) values ('%d', '%s', '%s','%s', '%s')" % (hjson['results'][0]['artistId'], conn.escape_string(hjson['results'][0]['artistName']), \
		hjson_sellerUrl,str_time, str_time))


	genres_count = 0
	for genres_string in hjson['results'][0]['genres']:
		genres_count+=1


	for genres_id in range(0, genres_count):
		# print hjson['results'][0]['genres'][genres_id]
		# print hjson['results'][0]['genreIds'][genres_id]
		tb_category = ("insert into tb_category (category_id, category_name, created_at, updated_at) values ('%d', '%s','%s', '%s')" % (int(hjson['results'][0]['genreIds'][genres_id]), hjson['results'][0]['genres'][genres_id], \
		str_time, str_time))

		tb_app_category = ("insert into tb_app_category (app_id, category_id, created_at, updated_at) values ('%d', '%d','%s', '%s')" % (hjson['results'][0]['trackId'], int(hjson['results'][0]['genreIds'][genres_id]), \
		str_time, str_time))

		try: 
			cur.execute(tb_category)
			cur.execute(tb_app_category)
		except MySQLdb.IntegrityError, e:
			pass




	cur.execute(tb_rank)
	try: 
		cur.execute(tb_app)
		cur.execute(tb_company)
	except MySQLdb.IntegrityError, e:
		pass


	
conn.commit()
cur.close()
conn.close()



