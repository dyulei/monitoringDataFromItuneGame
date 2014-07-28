#coding=utf-8
import urllib
import re

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def writeFile(html):
	file_object = open('/Users/Levi/github/python/test_web.html', 'w')
	file_object.write(html)
	file_object.close()

html = getHtml("https://itunes.apple.com/cn/rss/topfreeapplications/limit=10/genre=6014/json")
writeFile(html)




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