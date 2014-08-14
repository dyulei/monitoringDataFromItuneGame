#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json

#machine=["192.168.0.92", "192.168.0.94"]

def get_machine():
    try:
        f = open("machine.json")
        return json.dumps(json.load(f))
    except IOError,e:
        print e

#    en = json.JSONEncoder(ensure_ascii=False, encoding="utf-8")
#    return en.encode(machine) 

if __name__ == "__main__":
    print  get_machine()

