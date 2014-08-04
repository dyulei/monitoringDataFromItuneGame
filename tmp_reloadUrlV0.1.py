import urllib
import re
import json
import urllib2
import os
import time
import threading


def download(url_itune, url_kind):
	str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	try: 
		html = urllib2.urlopen(r'%s' % url_itune)
	except urllib2.URLError, e:
		print e.code
		if e.code != 200:
			download(url_itune, url_kind)


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

		try: 
			html1 = urllib2.urlopen(URL)
		except urllib2.URLError, e:
			print e.code
			if e.code != 200:
				try: 
					html1 = urllib2.urlopen(URL)
				except urllib2.URLError, e:
					print e.code
					break

		hjson1 = json.loads(html1.read())
		s = hjson1['results'][0]['trackName']
		file_object.write("%3d : " % x)
		file_object.write(s.encode("gb2312","ignore"))
		file_object.write("\n")
		print "read %d" % x
		urllib.urlretrieve(URL, './%s/%d.html' % (file_name, x))
		x+=1
	file_object.close()


download('https://itunes.apple.com/cn/rss/topfreeapplications/limit=200/genre=6014/json', 'Free')

# download('http://bbs.csdn.net/callmewhy', 'Free')
