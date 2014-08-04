#coding=utf-8
import urllib
import re
import json
import urllib2
import os
import time
import threading

# str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# if os.path.isdir("%s" % str_time):
# 	print 'The path is exist !'
# else : 
# 	os.mkdir("%s" % str_time)
# 	print 'creat over'


def download(url_itune, url_kind):
	str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	html = urllib2.urlopen(r'%s' % url_itune)
	hjson = json.loads(html.read())
	print 'analysis the json data'
	file_name = '%s%s' % (str_time,url_kind)
	if os.path.isdir("%s" % file_name):
		print 'The path is exist !'
	else : 
		os.mkdir("%s" % file_name)
		print 'creat over'

	file_object = open('%s.txt' % file_name, 'a+')
	file_object.write("The %s Game Rank, int the date : %s\n" % (url_kind,str_time))
	x = 1
	for i in hjson['feed']['entry']:
		URL = "https://itunes.apple.com/cn/lookup?id=" + i['id']['attributes']['im:id']
		html1 = urllib2.urlopen(URL)
		hjson1 = json.loads(html1.read())
		s = hjson1['results'][0]['trackName']
		file_object.write("%3d : " % x)
		file_object.write(s.encode("gb2312","ignore"))
		file_object.write("\n")
		print "read %d" % x
		urllib.urlretrieve(URL, './%s/%d.html' % (file_name, x))
		x+=1
	file_object.close()

# html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/toppaidapplications/limit=200/genre=6014/json')

# download('https://itunes.apple.com/cn/rss/topfreeapplications/limit=200/genre=6014/json', 'Free')
# download('https://itunes.apple.com/cn/rss/toppaidapplications/limit=200/genre=6014/json', 'Paid')
# download('https://itunes.apple.com/cn/rss/topgrossingapplications/limit=200/genre=6014/json', 'Grossing')

t1 = threading.Thread(download('https://itunes.apple.com/cn/rss/topfreeapplications/limit=200/genre=6014/json', 'Free'))
t2 = threading.Thread(download('https://itunes.apple.com/cn/rss/toppaidapplications/limit=200/genre=6014/json', 'Paid'))
t3 = threading.Thread(download('https://itunes.apple.com/cn/rss/topgrossingapplications/limit=200/genre=6014/json', 'Grossing'))
t1.start()
t2.start()
t3.start()



# hjson = json.loads(html.read())
# print hjson
# # URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
# print 'json analyse'
# file_object = open('rank_Paid', 'a+')
# file_object.write("The free Game Rank\n")
# x = 1
# for i in hjson['feed']['entry']:
# 	if (i == 3):
# 		break
# 	URL = "https://itunes.apple.com/cn/lookup?id=" + i['id']['attributes']['im:id']
# 	html1 = urllib2.urlopen(URL)
# 	hjson1 = json.loads(html1.read())
# 	s = hjson1['results'][0]['trackName']
# 	file_object.write("%3d : " % x)
# 	file_object.write(s.encode("gb2312","ignore"))
# 	file_object.write("\n")
# 	print "read %d" % x
# 	urllib.urlretrieve(URL, './14.7.30/%d.html' % x)
# 	x+=1
# file_object.close()	