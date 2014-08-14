#!/usr/bin/env python
#-*- coding:utf-8 -*-

from cStringIO import StringIO
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class Field:
    def __init__(self, name, value, is_file = False):
        self.name = name
        self.value = value
        self.is_file = is_file


class MultiPart(object):
    def __init__(self, boundary, content):
        self.field = {}
        fields = content.split(boundary)

        for field in fields:  
            if len(field) < 5:
                continue

            data = StringIO(field)

            data.readline()
            field_head = data.readline()
            name = field_head[field_head.find("name=") + 5:-2]
            if name.find(";") != -1:
                name = name[:name.find(";")]
                data.readline()
                data.readline()

                value = data.read(len(field))
                print "v:" + value
                value = value[:-2]
                self.field[name] = value 
            else:
                data.readline()
                value = data.readline().rstrip("\r\n")
                self.field[name] = value 

    def __getitem__(self, key):
        return self.field[key]
    def __str__(self):
        return str(self.field)
        
