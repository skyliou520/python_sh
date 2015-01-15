#! /usr/bin/python
import sys
import httplib
import base64

for arg in sys.argv:
    print arg

connection = httplib.HTTPConnection(sys.argv[1],80)
base64string = base64.encodestring('%s:%s' % (sys.argv[2], sys.argv[3])).replace('\n', '')
headers ={"Authorization":"Basic %s" % base64string}
print headers
#requests.get(connection, auth=(sys.argv[2],sys.argv[3] ))
connection.request('GET',"/cgi-bin/videoRecord.cgi?action=get","",headers)
response = connection.getresponse()
print response.status, response.reason, response.read()

