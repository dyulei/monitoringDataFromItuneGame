import urllib
import re
import json
import urllib2


# fhtml = open('2014-08-04Free/1.html', 'r')


for i in range(1, 4):
	html = open('/Users/Levi/github/monitoringDataFromItuneGame/14.7.30free/%d.html' % i , 'r')
	hjson = json.loads(html.read())
	# print hjson
	print hjson['results'][0]['trackName']
# hjson = json.loads(html.read())
# print hjson['feed']['entry'][0]['id']['attributes']['im:id']
# URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
