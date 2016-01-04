# ArcFare
WAF bypass toolkit

# Usage
python arcfare.py -option<br>
<pre>
  -h		              - display this dialog
  -r host		          - resolve ip address of given host
  -p host iphost		  - start an arcfare direct proxy to the target
</pre>

# How it works?
## Resolving
It will check an element in the index using the domain name for connection, then it will try to connect to the IP retrieved from a common name (like server.site.net) and checks if indexes match (Using conn.putheader("Host", host) we can tell the webserver that we want the website "domain.net" but using the direct ip in order to avoid issue with virtual hosting servers)
## Proxy
Now with the real IP we can build a local webserver that forwards our request to the remote server changing the host header of every incoming request. (It will also change every url that match to the domain name with localhost:port so crawlers will ask the proxy for every resources)
