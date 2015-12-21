# Code by @Arm4x

import httplib, socket, requests, sys
from bs4 import BeautifulSoup

debug = False

def debug_print(string):
    if(debug == True):
        print "[Debug] "+string

def get_title_tag(host):
    debug_print("[i] using <title> for check, analyzing...")
    page = requests.get('http://'+host)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")
    debug_print("[i] title: " + soup.title.string)
    return soup.title.string

def check(ip,host,stringcheck):
    debug_print("[i] performing check on ip: " + ip)
    conn = httplib.HTTPConnection(ip)
    conn.putrequest("GET", "/", skip_host=True)
    conn.putheader("Host", host)
    conn.endheaders()
    res = conn.getresponse()
    html = res.read()
    soup = BeautifulSoup(html, "html.parser")
    debug_print("[i] domain title: " + stringcheck + " ip title: " + soup.title.string)
    if(soup.title.string == stringcheck):
        return True
    else:
        return False

def check_if_cloudflare(ip):
    debug_print("[i] cloudflare check...")
    page = requests.get('http://'+ip)
    html = page.content
    soup = BeautifulSoup(html, "html.parser")
    if("Direct IP access not allowed" in soup.title.string):
        debug_print("[x] cloudflare detected")
        return True
    return False

def resolve_domain(domain,title):
    list = open('list.txt')
    common = list.read().split("\n")
    i = 0
    while i < len(common):
        level = 0
        url = common[i] + "." + domain
        debug_print("[i] trying: " + url)
        try:
            ip = socket.gethostbyname(url)
            if(check_if_cloudflare(ip)==False):
                level = 1
                
                if(check(ip,domain,title) == True):
                    print("[i] Direct ip to target found: " + ip)
                    level = 2
                
                if(level == 1):
                    print("[i] Direct ip found: " + ip + " but target seems different")
                    x = raw_input("Do you want to keep testing the others (if any)?(Y/n)")
                    if((x=="n") or (x=="N")):
                        sys.exit()
                    else:
                        pass
    
                if(level == 2):
                    print("[i] Direct ip to target found: " + ip)
                    x = raw_input("Do you want to keep testing the others (if any)?(y/N)")
                    if((x=="y") or (x=="Y")):
                        pass
                    else:
                        sys.exit()
    
        except socket.gaierror:
            debug_print("[x] invalid url: " + domain + " skipping...")
        i = i+1
