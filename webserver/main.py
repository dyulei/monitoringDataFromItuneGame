#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import multipart

import machine
import business
import json
import os
import conf
import log_desc
import log_file
import timeLineV

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
 
class MyHandler(SimpleHTTPRequestHandler):
    '''web logical handler, include static/dynamic request'''

    def resp(self, body):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body)

        self.wfile.close()


    def do_GET(self):
        req = self.path.split("?")
        url_path=req[0]
        if url_path == '/ee':
            # bizid = req[1].split("=")[1]
            # path = conf.data_path + "/" + "7.json"            
            # path = conf.data_path + "/" +  "meta.xml"

            # f = open(path, "rb")
            # self.send_response(200)
            # self.send_header('Content-type', 'application/json')
            # fs = os.fstat(f.fileno())
            # self.send_header("Content-Length", str(fs[6]))
            # self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            # self.end_headers()
            # self.copyfile(f, self.wfile)   

            self.resp(json.dumps(timeLineV.get_timeLine(),  ensure_ascii = False))
            # f.close()
        else:
            return SimpleHTTPRequestHandler.do_GET(self)





    def do_POST(self):
        req = self.path
        n = self.headers.get("Content-Length")		
        buf = self.rfile.read(int(n))
        #print buf
        if req == '/get_machine':
            return self.resp( machine.get_machine())
        elif req == '/biz_list':
            return self.resp(business.get_business_list())
        elif req == '/log_meta':
            arg = json.loads(buf)
            bizid = arg["bizid"]
            path = conf.data_path + "/" + bizid + "/meta.xml"            
            #path = conf.data_path + "/" +  "meta.xml"
            f = open(path, "rb")
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            self.copyfile(f, self.wfile)        
        elif req == "/get_log_cat":
            #arg = json.loads(buf)
#           bizid = arg["bizid"]
            bizid = "cookierun"
            path = conf.data_path + "/" + bizid + "/meta.xml"            
            jstr = json.dumps(log_desc.get_log_cat(path),  ensure_ascii = False)
            print len(jstr)
            self.resp(str)
        elif req == "/get_data":
            arg = json.loads(buf)
            bizid = arg["bizid"]
            cat = arg["cat"]
            path = conf.data_path + "/" + bizid +  "/meta.xml"
            desc = log_desc.get_log_cat_detail(path, cat)
            data = log_file.get_log_by_cat(bizid, cat)
            self.resp(json.dumps({"desc": desc, "data": data},  ensure_ascii = False))
        elif req == "/new_biz":
            self.new_biz(buf)
            self.path = '/domainList.html'
            self.do_GET()

        elif req == '/dd':
            # arg = json.loads(buf)
            # path = conf.data_path + "/meta.xml"
            # desc = log_desc.get_log_cat_detail(path, cat)
            # data = log_file.get_log_by_cat(bizid, cat)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.resp(json.dumps({"desc": "dd", "data": "ee"},  ensure_ascii = False))


            
def main():
    os.chdir(conf.page_path)
    try:
        server = HTTPServer(('', conf.port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'shutting down server...'
        server.socket.close()
	
if __name__	== '__main__':	
    main()
	
	
	
 