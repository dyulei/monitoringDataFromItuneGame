import urllib2  
req = urllib2.Request('http://bbs.csdn.net/callmewhy')  
      
try:  
    urllib2.urlopen(req)  
      
except urllib2.URLError, e:  
      
    print e.code 