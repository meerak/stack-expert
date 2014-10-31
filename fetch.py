import urllib2 
from urllib import urlopen
import simplejson as json
import zlib
import time

flag = True;
outfile = open('users.txt', 'w')

pagesize=100
page = 1
while(flag):

	stackoverflow_url = 'https://api.stackexchange.com/2.2/users?fromdate=1293840000&todate=1412121600&order=asc&sort=reputation&site=stackoverflow&key=64lUgQSpgbBaPuIqMwbyJw((&page=' + str(page) + '&pagesize=' + str(pagesize)
	url = urllib2.urlopen(stackoverflow_url)
	decompressed_data=zlib.decompress(url.read(), 16+zlib.MAX_WBITS)
	#json_data = open('users.txt')
	data = json.loads(decompressed_data)
	x = json.dumps(data['items'])
	outfile.write(x[1:-1])
	if(data['has_more'] == False):
	 	flag = False
	 	break
	page = page+1
	outfile.write(",")
	backoff = 1
	if 'backoff' in data:
		backoff  = data['backoff'] + 1;
	print page, data['quota_remaining'], backoff
	time.sleep(backoff);
	

outfile.close();


  
