#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

d = 'duanyulei'
data = [{'a':'%s' % d, 'b':(2,4), 'c':3.0}]
print 'DATA:', repr(data)

unsorted = json.dumps(data)
print 'JSON:', json.dumps(data)
print 'SORT:', json.dumps(data, sort_keys=True)
print 'INDENT:', json.dumps(data, sort_keys=True, indent=2)

