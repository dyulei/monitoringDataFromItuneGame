#coding=utf-8
import urllib
import re
import json
import urllib2
# import sys

# def getHtml(url):
# 	page = urllib.urlopen(url)
# 	html = page.read()
# 	return html

# def writeFile(html):
# 	file_object = open('/Users/Levi/github/python/test_web.html', 'w')
# 	file_object.write(html)
# 	file_object.close()

# def writeJSONFile(html):

# 	hjson = json.loads(html.read())
# 	print hjson['feed']['entry'][0]['im:name']['label']



# Filehtml = getHtml("https://itunes.apple.com/cn/rss/topfreeapplications/limit=10/genre=6014/json")
html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/topfreeapplications/limit=200/genre=6014/json')
hjson = json.loads(html.read())
print hjson
# URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
print 'json analyse'
file_object = open('rank_Free', 'a+')
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
	# urllib.urlretrieve(URL, './14.7.30/%d.html' % x)
	x+=1
file_object.close()	
	# file_object = open('/Users/Levi/github/monitoringDataFromItuneGame/test_web.html', 'w')
	# file_object.write(page)
	# file_object.close()

# html_URL = urllib2.urlopen(URL)
# hjson1 = json.loads(html_URL.read())
# print hjson1['results'][0]['trackName']


#writeJSONFile(html)



# writeFile(html)

# 	x = 0
# 	for imgurl in imglist:
# 		urllib.urlretrieve(imgurl, '%s.jpg' % x)
# 		x+=1


# f = file('hello', "w")
# html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/topgrossingapplications/limit=10/genre=6014/json')

# hjson = json.loads(html.read())

# print hjson['feed']['entry'][0]['im:name']['label']


# f.write(a)
# print hjson['images']['large']
# print hjson['summary']






# def getHtml(url):
# 	page = urllib.urlopen(url)
# 	html = page.read()
# 	return html

# def getImg(html):
# 	reg = r'src="(.+?\.jpg)" pic_ext'
# 	imgre = re.compile(reg)
# 	imglist = re.findall(imgre,html)
# 	# return imglist
# 	x = 0
# 	for imgurl in imglist:
# 		urllib.urlretrieve(imgurl, '%s.jpg' % x)
# 		x+=1

# html = getHtml("http://tieba.baidu.com/p/2738151262")

# print getImg(html)