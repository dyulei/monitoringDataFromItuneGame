#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

port = 8080 
page_path = "/Users/Levi/github/monitoringDataFromItuneGame/webserver/"
data_path = "/Users/Levi/github/monitoringDataFromItuneGame/webserver/business"

