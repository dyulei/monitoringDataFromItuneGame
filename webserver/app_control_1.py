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
import datetime



def get_data():

    try:
        conn = MySQLdb.connect(host="121.201.10.15",
                    user='eagleeye',
                    passwd='EYeapp$ea@2',
                    db="db_rankapp",
                    port=30013)
    except OperationalError, e:
        print 'OperationalError...'
        pass
    cur = conn.cursor()
    reload(sys)
    sys.setdefaultencoding('utf8')
    conn.set_character_set('utf8')


    
    tb_rank_orderby_releasetime = ("select * from db_rankapp.tb_rank t where t.created_at >= '2014-08-01' and t.created_at <= '2014-08-09' and t.rank_type = 1 order by app_id")

    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()

    startDate = '2014-08-01'
    endDate = '2014-08-09'
    startLine = time.mktime(datetime.datetime(start[0:4],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple())

    print rank[1]

    for rank in recs:
        app_id = rank[1]
        created_at = rank[4]
        rank_num = rank[3]




    #     lisDic = {}
    #     lisDic['date'] = rank[2][0:10]
    #     lisDic['text'] = rank[0]
    #     lisDic['icon'] = rank[1]
    #     listArr.append(lisDic)

    # total = len(listArr)

    # data = {}

    # data['status'] = 0
    # data['message'] = ''
    # data['data'] = {}
    # data['data']['total'] = total
    # data['data']['list'] = listArr
    cc=[2014,8,3,0,0,0] 
    c1 = time.mktime(datetime.datetime(cc[0],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple())

    cc=[2014,8,4,0,0,0] 
    c2 = time.mktime(datetime.datetime(cc[0],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple())

    cc=[2014,8,5,0,0,0] 
    c3 = time.mktime(datetime.datetime(cc[0],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple())

    print c1 , c2, c3
    print c2 - c1, c3 - c2
    return data

if __name__ == "__main__":
    print  get_data()

    conn.commit()
    cur.close()
    conn.close()

