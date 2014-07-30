#coding=utf-8
import urllib
import re
import json
import urllib2


html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/toppaidapplications/limit=200/genre=6014/json')
hjson = json.loads(html.read())
print hjson
# URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
print 'json analyse'
file_object = open('rank_Paid', 'a+')
file_object.write("The free Game Rank\n")
x = 1
for i in hjson['feed']['entry']:
	if (i == 3):
		break
	URL = "https://itunes.apple.com/cn/lookup?id=" + i['id']['attributes']['im:id']
	html1 = urllib2.urlopen(URL)
	hjson1 = json.loads(html1.read())
	s = hjson1['results'][0]['trackName']
	file_object.write("%3d : " % x)
	file_object.write(s.encode("gb2312","ignore"))
	file_object.write("\n")

	print "read %d" % x
	urllib.urlretrieve(URL, './14.7.30/%d.html' % x)
	x+=1
file_object.close()	