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



    tb_rank_orderby_releasetime = ("select t.app_id, t.rank, t.created_at, a.app_name, a.icon_Url  from db_rankapp.tb_rank t, db_rankapp.tb_app a \
        where t.app_id = a.app_id and t.created_at >= '2014-08-06' and t.created_at <= '2014-08-07' and t.rank_type = 1 order by app_id")

    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()



    startDate = datetime.datetime.strptime('2014-08-06', '%Y-%m-%d')
    endDate = datetime.datetime.strptime('2014-08-07', '%Y-%m-%d')

    print startDate, endDate

    dd = endDate - startDate
    diftime =  dd.days
    print diftime


    tmp_id = 'null'
    maxValue = 0
    minValue = 201
    maxDate = minDate = startDate

    preDate = endDate
    for rank in recs:
        app_id = rank[0]
        created_at = datetime.datetime.strptime(str(rank[2])[0:10], '%Y-%m-%d')
        rank_num = rank[1]

        if(app_id != tmp_id):

            if preDate != endDate:
                maxValue = 201
                maxDate = created_at

            #
            if maxValue != 0:
                # print minDate, maxDate
                # print minValue , maxValue
                # print tmp_id
                if (minDate - maxDate).days < 0:
                    # print minDate, maxDate
                    print tmp_id
                    print maxValue - minValue
                    


            #
            maxValue = 0
            minValue = 201

            if (created_at - startDate).days != 0:
                maxValue = 201
                maxDate = created_at

            if rank_num <= minValue:
                minValue = rank_num
                minDate = created_at

            if rank_num >= maxValue:
                maxValue = rank_num
                maxDate = created_at
            tmp_id = app_id

        else:
            if (created_at - preDate).days != 1:
                maxValue = 201
                maxDate = created_at
            
            if rank_num <= minValue:
                minValue = rank_num
                minDate = created_at

            if rank_num >= maxValue:
                maxValue = rank_num
                maxDate = created_at

        preDate = created_at

    if(app_id == tmp_id):
        print minDate, maxDate
        print minValue , maxValue
        print tmp_id

        # print rank_num
        # print created_at
        # print created_at[0:7]
        # dd_time = time.strftime('%Y-%m-%d', created_at[0:10])

        # dd_time = datetime.datetime.strptime(created_at[0:10], '%Y-%m-%d')
        # print dd_time
        # print created_at[0:10]
        # d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
        

        # today = datetime.datetime(*time.localtime()[:6])
    # t = datetime.timedelta(days = 2)


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


    return data

if __name__ == "__main__":
    print  get_data()

    conn.commit()
    cur.close()
    conn.close()

