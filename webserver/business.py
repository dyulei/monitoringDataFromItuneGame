#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import sys
import conf

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# all business list
_bizs = []

#
biz_list_file = conf.data_path + "/biz_list.json"

class Business(object):
    def __init__(self, id, name, log_svr):
        self.id = id
        self.name = name
        self.log_svr = log_svr

    def __getitem__(self, name):
        if name == "id":
            return self.id

def bizDecoder(dict):
    if "id" in dict:
        return Business(dict["id"], dict["name"], dict["log_svr"])
    return dict


class BizEncoder(json.JSONEncoder):    
    def __init__(self, **kw):
        if "ensure_ascii" in kw:
            del kw["ensure_ascii"]
        return json.JSONEncoder.__init__(self, ensure_ascii=False, **kw)               
    
    def default(self, o):
        if isinstance(o, Business):
            return {"id": o.id, "name": o.name, "log_svr": o.log_svr}
        raise TypeError

def get_business_list():        
    load(biz_list_file)
    return json.dumps(_bizs, cls=BizEncoder)


def load(filename):
    global _bizs
    _bizs = []
    
    try:
        f = open(filename)
        _bizs = json.load(f,object_hook=bizDecoder)
    except IOError,e:
        print e

def store(filename):
    try:
        f = open(filename, "w")
        json.dump(_bizs, f, cls=BizEncoder)
        f.close()
    except IOError,e:
        print e

def modify_business(o):
    exist = False
    for i in range(len(_bizs)):
        if _bizs[i].id == o.id:
            exist = True
            _bizs[i] = o
            store(biz_list_file)
            break
    if not exist:
        _bizs.append(o)
        store(biz_list_file)
        

get_business_list()

if __name__ == "__main__":
    '''
    _bizs.append(Business("8ball", "8个球", "10.1.0.1"))
    _bizs.append(Business("cookierun","姜饼人", "10.1.1.1"))
    store("./b.json")
    '''
    print  get_business_list()
#    store("./c.json")


