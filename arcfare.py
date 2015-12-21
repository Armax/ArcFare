# Code by @Arm4x

import scloud, sproxy, sys

if(len(sys.argv) < 2):
    print "Usage: python arcfare.py [options]"
    print
    print "Use -h for help"
    sys.exit()

print "--== arcfare, developed by: @Arm4x ==--"

if(sys.argv[1] == "-h"):
    print "--== arcfare command list ==--"
    print
    print "-h\t\t- display this dialog"
    print "-r host\t\t- resolve ip address of given host"
    print "-p host iphost\t\t- start an arcfare direct proxy to the target"

elif(sys.argv[1] == "-r"):
    host = sys.argv[2]
    print "[i] searching direct ip..."
    scloud.resolve_domain(host,scloud.get_title_tag(host))

elif(sys.argv[1] == "-p"):
    host = sys.argv[2]
    ip = sys.argv[3]
    sproxy.start(host,ip)

else:
    print "--== arcfare command list ==--"
    print
    print "-h\t\t- display this dialog"
    print "-r host\t\t- resolve ip address of given host"
    print "-p host iphost\t\t- start an arcfare direct proxy to the target"