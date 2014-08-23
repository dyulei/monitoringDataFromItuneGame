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



    tb_rank_orderby_releasetime = ("select t.app_id, t.rank, t.created_at from db_rankapp.tb_rank t \
        where t.created_at >= '%s' and t.created_at <= '%s' and t.rank_type = '%s' order by app_id" % (start, end, app_type))

    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()



    startDate = datetime.datetime.strptime('%s' % start, '%Y-%m-%d')
    endDate = datetime.datetime.strptime('%s' % end, '%Y-%m-%d')


    tmp_id = 'null'
    maxValue = 0
    minValue = 201
    maxDate = minDate = startDate
    app_id_str = ""
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
                if (minDate - maxDate).days < 0:
                    # print tmp_id
                    app_id_str += ',%s' % tmp_id
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

    if app_id == tmp_id and  (minDate - maxDate).days < 0:
        # if (minDate - maxDate).days < 0:
        app_id_str += ',%s' % tmp_id
        # print maxValue - minValue
        # lisDic = {}
        # lisDic['app_id'] = tmp_id
        # lisDic['text'] = rank[3]
        # lisDic['icon'] = rank[4]
        # lisDic['num'] = int(maxValue - minValue)
        # listArr.append(lisDic)

    # print app_id_str[1:]
    tb_rank_category_id = ("select t.category_id, c.category_name,count(1) num from (select * from tb_app_category group by category_id,app_id) t, \
        tb_category c where t.app_id in (%s) and t.category_id >= 7000 and c.category_id = t.category_id group by c.category_name" % app_id_str[1:])

    cur.execute(tb_rank_category_id)
    recs = cur.fetchall()
    for dlist in recs:
        lisDic = []
        lisDic.append(dlist[1])
        lisDic.append(dlist[2])
        listArr.append(lisDic)


    data = {}
    data['status'] = 0
    data['message'] = 'success'
    data['data'] = {}
    data['data']['columns'] = ["category_name", "num"]
    data['data']['alias'] = {}
    data['data']['list'] = listArr


    return data

if __name__ == "__main__":
    print  get_data('2014-08-06', '2014-08-07', '0')


    # cur.close()
    # conn.close()

