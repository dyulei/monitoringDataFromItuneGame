#!/usr/bin/env python
#-*- coding:utf-8 -*-
from xml.etree import ElementTree 


class LogFieldDesc(object):
    '''日志字段对应的描述符，当前包括字段名,描述，暂未处理类型'''
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
class LogFieldDescTbl(object):
    '''日志类别对应的描述符表  '''
    def __init__(self, cat):
        self.name = cat.name
        self.tbl = [cat,]
    def __len__(self):
        return len(self.tbl)
    def append(self, field):
        self.tbl.append(field)
            
                    
#所有日志类别描述符表，日志类别->LogFieldDescTbl               
log_fields={}

def get_log_cat_detail(filename, cat):
    read_xml(open(filename).read())
    details = []
    for v in log_fields.itervalues():
        if v.name == cat:
            for n in range(len(v.tbl)):
                details.append({"name": v.tbl[n].name, "desc": v.tbl[n].desc})
            break
    return details

def get_log_cat(filename):
    read_xml(open(filename).read())
    cats = []
    for v in log_fields.itervalues():
        cats.append({"name": v.name, "desc": v.tbl[0].desc})
    return cats

def handle_elems(elems, new_tbl):
    '''将日志描述里面的element元素追加到日志字段描述符表里面'''
    for e in elems:
        field = LogFieldDesc(e.attrib['name'], e.attrib['desc'])
        new_tbl.append(field)           
            
        
def handle_node(node):
    '''处理struct，暂不支持嵌套结构'''
    head_field = LogFieldDesc(node.attrib['name'], node.attrib['desc'])
    new_tbl = LogFieldDescTbl(head_field)
        
    elems = node.getchildren()
    handle_elems(elems, new_tbl)
    
    log_fields[head_field.name] = new_tbl    
    

   

def read_xml(text):
    global log_fields
    log_fields={}
    '''读xml文件,暂未处理错误格式的xml'''
    root = ElementTree.fromstring(text)
    
    # 遍历解析struct元素    
    lst_node = root.getiterator("struct")
    for node in lst_node:
        handle_node(node)

def dump_cat(desc_tbl):
    for field in desc_tbl.tbl:
        print field.name, field.desc
        
def dump_all_cat():
    for k in log_fields:
        print "==========================================="
        print k, len(log_fields[k])
        dump_cat(log_fields[k]) 

if __name__ == '__main__':  
#     read_xml(open("/share/zh/business/meta.xml").read())
#     dump_all_cat()
     print get_log_cat("/share/zh/business/meta.xml")
#     print get_log_cat_detail("/share/zh/business/meta.xml")

