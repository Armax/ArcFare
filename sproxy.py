# Code by @Arm4x

import httplib, socket, requests, sys, threading, urllib
from bs4 import BeautifulSoup
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn

PORT_NUMBER = 1338
host = "a"
ip = "1"

debug = False
use_proxies = True

def debug_print(string):
    if(debug == True):
        print "[Debug] "+string

def get_page(page):
    conn = httplib.HTTPConnection(ip, timeout=10)
    conn.putrequest("GET", page, skip_host=True)
    conn.putheader("Host", host)
    conn.endheaders()
    res = conn.getresponse()
    return res.read().replace(host, "localhost:"+str(PORT_NUMBER))

def post_page(page, contents):
    headers = {"Host": host, "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(ip, timeout=10)
    conn.request("POST", page, contents, headers)
    res = conn.getresponse()
    return res.read().replace(host, "localhost:"+str(PORT_NUMBER))

class proxy(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(get_page(self.path))
        return

    def do_POST(self):
        content_length = self.headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        content = self.rfile.read(length)
        self.wfile.write(post_page(self.path, content))
        self.send_response(200)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """threading"""

def start(a,b):
    global host
    global ip
    host = a
    ip = b
    try:
        server = ThreadedHTTPServer(('', PORT_NUMBER), proxy)
        print '[i] Started sproxy on port ' , PORT_NUMBER
        print 'sproxy -> ' + ip

        server.serve_forever()

    except KeyboardInterrupt:
        print 'shutting down...'