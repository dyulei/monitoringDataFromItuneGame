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

def get_data(startdate, enddate):


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


    tb_rank_orderby_releasetime = ("SELECT 月份, sum(上线数) AS '上线数', sum(top20) AS 'top20' \
    FROM \
        ( \
            ( \
                SELECT \
                    DATE_FORMAT(date, '%%Y-%%m') AS '月份', \
                    count(DISTINCT app_id) AS '上线数', \
                    0 AS 'top20' \
                FROM \
                    tb_v_app a \
                WHERE \
                    DATE_FORMAT(date, '%%Y-%%m') BETWEEN '%s' \
                AND '%s' \
                GROUP BY \
                    DATE_FORMAT(date, '%%Y-%%m') \
                ORDER BY \
                    月份 ASC \
            ) \
            UNION ALL \
                ( \
                    SELECT \
                        DATE_FORMAT(date, '%%Y-%%m') AS '月份', \
                        0 AS '上线数', \
                        count(DISTINCT app_id) AS 'top20' \
                    FROM \
                        tb_v_app \
                    WHERE \
                        DATE_FORMAT(date, '%%Y-%%m') BETWEEN '%s' \
                    AND '%s' \
                    AND app_id IN ( \
                        SELECT DISTINCT \
                            app_id \
                        FROM \
                            tb_rank \
                        WHERE \
                            rank <= 20 \
                    ) \
                    GROUP BY \
                        DATE_FORMAT(date, '%%Y-%%m') \
                    ORDER BY \
                        date ASC \
                ) \
        ) a GROUP BY 月份 order by 月份" % (startdate, enddate,startdate, enddate))


    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()
    listArr = []

    for rank in recs:
        lisDic = []
        lisDic.append(rank[0])
        lisDic.append(int(rank[1]))
        lisDic.append(int(rank[2]))
        listArr.append(lisDic)

    # def cmp1(x, y):
    #     if x[0] > y[0]:
    #         return 1
    #     elif x[0] < y[0]:
    #         return -1
    #     else: return 0

    # listArr.sort(cmp = cmp1)

    data = {}
    data['status'] = 0
    data['message'] = 'success'
    data['data'] = {}
    data['data']['columns'] = ["日期", "上线数量", "Top20"]
    data['data']['alias'] = {}
    data['data']['list'] = listArr
    return data

if __name__ == "__main__":
    print  get_data()
    conn.commit()
    cur.close()
    conn.close()


