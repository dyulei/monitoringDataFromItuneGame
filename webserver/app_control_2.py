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

def cmp1(x, y):
    if x['num'] < y['num']:
        return 1
    elif x['num'] > y['num']:
        return -1
    else: return 0

def get_data(start, end, app_type):

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
        where t.app_id = a.app_id and t.created_at >= '%s' and t.created_at <= '%s' and t.rank_type = '%s' order by app_id" % (start, end, app_type))

    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()



    startDate = datetime.datetime.strptime('%s' % start, '%Y-%m-%d')
    endDate = datetime.datetime.strptime('%s' % end, '%Y-%m-%d')

    print startDate, endDate

    dd = endDate - startDate
    diftime =  dd.days
    print diftime


    tmp_id = 'null'
    maxValue = 0
    minValue = 201
    maxDate = minDate = startDate

    preDate = endDate
    listArr = []
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
                if (minDate - maxDate).days > 0:
                    # print minDate, maxDate
                    # print tmp_id
                    # print maxValue - minValue
                    lisDic = {}
                    lisDic['app_id'] = tmp_id
                    lisDic['text'] = rank[3]
                    lisDic['icon'] = rank[4]
                    lisDic['num'] = int(maxValue - minValue)
                    listArr.append(lisDic)
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

    if app_id == tmp_id and  (minDate - maxDate).days > 0:
        # if (minDate - maxDate).days < 0:
        print tmp_id
        print maxValue - minValue
        lisDic = {}
        lisDic['app_id'] = tmp_id
        lisDic['text'] = rank[3]
        lisDic['icon'] = rank[4]
        lisDic['num'] = int(maxValue - minValue)
        listArr.append(lisDic)



    data = {}
    listArr.sort(cmp=cmp1)
    data['status'] = 0
    data['message'] = 'success'
    data['data'] = {}
    data['data']['list'] = listArr


    return data

if __name__ == "__main__":
    print  get_data('2014-08-06', '2014-08-07', '0')


    # cur.close()
    # conn.close()

