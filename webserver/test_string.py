
date_string = '2012-10'
dd = ("SELECT t.app_name, t.icon_Url, t.release_date FROM db_rankapp.tb_app t where release_date like \'%%%s%%\' order by release_date" % date_string)
print dd