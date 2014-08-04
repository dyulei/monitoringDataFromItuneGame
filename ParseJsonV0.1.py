import urllib
import re
import json
import urllib2


# fhtml = open('2014-08-04Free/1.html', 'r')
html = open('/Users/Levi/github/monitoringDataFromItuneGame/14.7.30free/1.html', 'r')

# hjson = json.loads(html.read())
# print hjson['feed']['entry'][0]['id']['attributes']['im:id']
# URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
hjson = json.loads(html.read())
print hjson

print hjson['results'][0]['trackName']
# print hjson
# x = 0
# for i in hjson['feed']['entry']:
# 	URL = "https://itunes.apple.com/cn/lookup?id=" + i['id']['attributes']['im:id']

# 	# hjson1 = json.loads(html_URL.read())
# 	# print hjson1['results'][0]['trackName']
# 	print 'read x'
# 	urllib.urlretrieve(URL, '%s.html' % x)
# 	x+=1

