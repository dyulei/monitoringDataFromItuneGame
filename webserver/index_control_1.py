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


# conn = MySQLdb.connect(host="121.201.10.15",
#             user='eagleeye',
#             passwd='EYeapp$ea@2',
#             db="db_rankapp",
#             port=30013)
# cur = conn.cursor()
# reload(sys)
# sys.setdefaultencoding('utf8')
# conn.set_character_set('utf8')

def get_data(startdate, overdate):
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





    tb_rank_orderby_releasetime = ("\
        SELECT\
        left(月份,4) as 'year',\
      right(月份,2) as 'month',\
        sum(上线数) AS 'online',\
        sum(top20) AS 'top',\
    IF (\
        (sum(top20) + 5) > 20, \
        20, \
        sum(top20) + 5 \
    ) AS 'size' \
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
            )\
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
                    AND app_id IN (\
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
                )\
        ) a \
    GROUP BY 月份 order by 月份" % (startdate, overdate, startdate, overdate))

    # print tb_rank_orderby_releasetime

    cur.execute(tb_rank_orderby_releasetime)
    recs = cur.fetchall()

    listArr = []
    for rank in recs:
        lisDic = {}
        lisDic['year'] = rank[0]
        lisDic['month'] = rank[1]
        lisDic['online'] = int(rank[2])
        lisDic['top'] = int(rank[3])
        lisDic['size'] = int(rank[4])
        listArr.append(lisDic)


    total = len(listArr)

    data = {}

    data['status'] = 0
    data['message'] = ''
    data['data'] = {}
    data['data']['total'] = total
    data['data']['list'] = listArr
    return data

if __name__ == "__main__":
    print  get_data('2014-04', '2014-07')
    conn.commit()
    cur.close()
    conn.close()
