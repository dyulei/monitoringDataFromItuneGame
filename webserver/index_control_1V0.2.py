#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
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


tb_rank_orderby_releasetime = ("SELECT t.app_name, t.icon_Url, t.release_date, krank.rank FROM db_rankapp.tb_app t,db_rankapp.tb_rank krank where t.app_id=krank.app_id order by release_date")
cur.execute(tb_rank_orderby_releasetime)
recs = cur.fetchall()

size = 5
count = 0
count_top = 0
listArr = []
tmp_year = -1
tmp_month = -1

for rank in recs:
    lisDic = {}
    if (tmp_year == rank[2][0:4]) and (tmp_month == rank[2][5:7]):
        count+=1
        if (rank[3]<=20):
            count_top+=1
        continue
    else:    
        if(tmp_year != -1):
            size += count_top
            if(size > 20): size = 20
            lisDic['size'] = size
            lisDic['year'] = tmp_year
            lisDic['month'] = tmp_month
            lisDic['online'] = count
            lisDic['top'] = count_top
            listArr.append(lisDic)

        # lisDic['date'] = rank[2]
        # lisDic['text'] = rank[0]
        # lisDic['icon'] = rank[1]
        count = 1
        count_top = 0
        size = 5
        if (rank[3]<=20):
            count_top = 1
        tmp_year = rank[2][0:4]
        tmp_month = rank[2][5:7]

size = 5
if(count > 1):
    size += count_top
    if(size > 20): 
        size = 20
    lisDic['size'] = size
    lisDic['year'] = rank[2][0:4]
    lisDic['month'] = rank[2][5:7]
    lisDic['online'] = count
    lisDic['top'] = count_top
    listArr.append(lisDic)

total = len(listArr)

data = {}

data['status'] = 0
data['message'] = ''
data['data'] = {}
data['data']['total'] = total
data['data']['list'] = listArr
# print data

conn.commit()
cur.close()
conn.close()


def get_data():
    return data

if __name__ == "__main__":
    print  get_data()
