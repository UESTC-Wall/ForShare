# -*- coding:utf-8 -*- 
import requests
import re
import urllib
from BeautifulSoup import BeautifulSoup
import mechanize
import cookielib


def gettitle(url):  
    try:
    	content = urllib.urlopen(url).read()
    	soup = BeautifulSoup(content)
    	print soup.find('title')
    	return soup.find('title') 

    	# _ = re.search('<title>(.*?)</title>', requests.get(url).content)  
     #    print url, _.group(1)  
     #    return _.group(1)
    except:  
        return u'暂无介绍'

def gettitle2(url):
	try: 
		print url
		br = mechanize.Browser()
		br.set_cookiejar(cookielib.LWPCookieJar()) # Cookie jar
		br.set_handle_equiv(True) # Browser Option
		br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 
		br.open(url)
		title=br.title()
		print title
		# print title.encode("utf-8")
		print title		
		return  title
	except:
		return u'暂无介绍'
