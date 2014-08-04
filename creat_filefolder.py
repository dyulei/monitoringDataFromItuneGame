import os
import time

str_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

if os.path.isdir("%s" % str_time):
	print 'The path is exist !'
else : 
	os.mkdir("%s" % str_time)
	print 'creat over'

