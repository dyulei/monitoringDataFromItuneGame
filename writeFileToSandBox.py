#coding=utf-8
import urllib
import re
import json
import urllib2
import sys

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



#html = getHtml("https://itunes.apple.com/cn/rss/topfreeapplications/limit=10/genre=6014/json")
html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/topfreeapplications/limit=10/genre=6014/json')
hjson = json.loads(html.read())
URL = "https://itunes.apple.com/cn/lookup?id=" + hjson['feed']['entry'][0]['id']['attributes']['im:id']
print URL

html_URL = urllib2.urlopen(URL)
hjson1 = json.loads(html_URL.read())
print hjson1['results'][0]['trackName']
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