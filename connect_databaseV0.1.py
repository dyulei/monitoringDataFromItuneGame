import MySQLdb
import sys, string, os

# try :
conn = MySQLdb.connect(host="121.201.10.15",
		user='eagleeye',
		passwd='EYeapp$ea@2',
		db="db_rankapp",
		port=30013)

# 		user='root',
# conn = MySQLdb.connect(host="localhost",
# 		passwd='',
# 		db="mysql",
# 		port=3306)

cur = conn.cursor()
dd = cur.execute('show tables')
result = cur.fetchall()
print result

count = cur.execute('show columns from tb_app')
print '%s' % count
result = cur.fetchall()
# print result


# cur.execute("insert into tb_rank (app_id,rank_type, rank, created_at, updated_at) values  ('3','2024', '4', '2013-11-11', '2013-11-11')")

# cur.execute("insert into tb_rank (app_id,rank_type, rank, created_at, updated_at) values  ('3','2024', '4', '2013-11-11', '2013-11-11')")

cur.execute("insert into tb_app (app_id, app_name, author, fit_Type, size, release_date, rom_type, description, icon_Url, trackViewUrl, download_url, filename, company_id, company_name, filemd5, star, created_at, updated_at, userRatingCount, bundleId, version, currency, price) \
	values ('100', 'adf', 'Tencent', 'iphone4', '9500', '2013-02-04', 'null', 'null', 'null', 'null', 'null', 'null', '12345', 'Tencent', 'NULL', '5', '2014-03-02', '2011-03-01', '12', '1234567', '4.0', '3', '12')")

conn.commit()
cur.close()
conn.close()

	# conn
# except Exception, e:
#     print e
#     sys.exit()


# conn=MySQLdb.connect(host="localhost",user="root",db="test")