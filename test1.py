#coding=utf-8
import urllib2
import json

html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')
# html = urllib2.urlopen(r'https://itunes.apple.com/cn/rss/topfreeapplications/limit=10/genre=6014/json')

hjson = json.loads(html.read())

# print hjson['feed']['entry'][0]['id']['attributes']['im:id']
print hjson
# print hjson['rating']
# print hjson['images']['large']
# print hjson['summary']
