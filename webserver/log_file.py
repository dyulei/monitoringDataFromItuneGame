#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import time
import re
from functools import partial
import conf
import log_desc


def check_all(fields):
	unknown_cat = set()
	fmt_wrong_logs = {}
	error_logs = []

	if len(fields) < 2:
		error_logs.append(fields)
		return
	
	cat = fields[0]	
	last_field = fields[len(fields)-1]
	last_field = last_field.rstrip('\n')
	fields[len(fields)-1] = last_field
	
	if log_desc.log_fields.has_key(cat):
		desctbl	= log_desc.log_fields[cat]
		if len(desctbl)	!= len(fields):
			if fmt_wrong_logs.has_key(cat):			
				fmt_wrong_logs[cat].append(fields)
			else:
				fmt_wrong_logs[cat]	= [fields]
			
	else:
		unknown_cat.add(cat)
		
	return unknown_cat, fmt_wrong_logs, error_logs


def check_log(fields, desctbl):
	cat = desctbl.name
	if fields[0] != cat:
		return None, False
		
	if (len(fields)	< 1):
		error_logs.append(fields)
		return None, False
	
	last_field = fields[len(fields)-1]
	last_field = last_field.rstrip('\n')
	fields[len(fields)-1] = last_field

	is_right =  True if len(desctbl) == len(fields) else False
	return fields, is_right

def get_log_by_cat_in_one_file(name, cat, max_count):
	'''获取文件name中的最近的类别为cat的日志，无论正确和错误, 最多max_count条'''
	logs=[]
	
	f = open(name)
	desctbl	= log_desc.log_fields[cat]
	for line in f:
		fields, yes = check_log(line.split('|'), desctbl)
		if fields is not None:
			logs.append((fields, yes))
		if len(logs) > max_count:
			break		
	f.close()
	return logs
								
def get_log_by_cat(bizid, cat, max_count = 100):
	files = get_log_files(bizid)
	'''获取文件name中的最近的类别为cat的日志，无论正确和错误, 最多max_count条'''
	all_logs=[]
	for f in files:
		logs =  get_log_by_cat_in_one_file(f, cat, max_count = 100)
		logs += all_logs		
		all_logs = logs
		if len(all_logs) >= max_count:
			break

	return all_logs
		 
def is_log_file(path, name):
	if len(name) - name.rfind(".log") != 4:
		return False
		
	m = re.search(path, name)
	if m is None:
		return False

	return True
		 
def is_log_path(subpath):
	if len(subpath) != len("20140625"):
		return False
	m = re.match(r'20[0-9]{2}[0-1][0-9][0-3][0-9]',subpath)
	if m is None:
		return False

	return True

def get_log_files(bizid):
	'''获取目录下的所有感兴趣的日志文件'''
#	root_path = "/data/game_log/" 

	files=[]
	root_path = conf.data_path 
	path = root_path + "/" + bizid
	now = time.localtime()
	log_subpath = filter(is_log_path, os.listdir(path))

	if len(log_subpath) > 2:
		log_subpath.sort()
		last_path = [log_subpath[-1], log_subpath[-2]]
		log_subpath = last_path
	for subpath in log_subpath:
		file_path = path + "/" + subpath				
		log_files = filter(partial(is_log_file, subpath), os.listdir(file_path))
		print log_files
		for f in log_files:
			fullname = file_path + "/" + f
			files.append(fullname)

	#按时间排序，便于处理最新的文件	
	files.sort(lambda x,y: cmp(x, y) * -1)
	return files
	
if __name__	== '__main__':		
	print get_log_files("biz")

	  
