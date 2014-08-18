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
tmp_date = -1

for rank in recs:
    lisDic = []
    if (tmp_date == rank[2][0:7]):
        count+=1
        continue
    else:    
        if(tmp_date != -1):
            # lisDic[0] = tmp_date
            # lisDic[1] = count
            lisDic.append(tmp_date)
            lisDic.append(count)
            listArr.append(lisDic)

        count = 1
        tmp_date = rank[2][0:7] 

if(count > 1):

    lisDic.append(tmp_date)
    lisDic.append(count)
    listArr.append(lisDic)

def cmp1(x, y):
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    else: return 0

listArr.sort(cmp = cmp1)

data = {}
data['status'] = 0
data['message'] = 'success'
data['data'] = {}
data['data']['columns'] = ["日期", "上线数量"]
data['data']['alias'] = {}
data['data']['list'] = listArr
# print data

conn.commit()
cur.close()
conn.close()


def get_data():
    return data

if __name__ == "__main__":
    print  get_data()



