from Wall.celery import app
from FundPart.models import *

import urllib2

@app.task
def hello_world():
    print('Hello World,fvf')

@app.task
def addtag(content):
	finallist = []
	if content[0:3]=='http':
		content = urllib2.urlopen(url).read()
	taglist = TagList.objects.all()
	for tag in taglist:
		num = content.count(tag[0].encode("utf-8"))
		if  num > 1:
			od[tag[0].encode("utf-8")]= num
    		print tag[0].encode("utf-8")
	tagdic = sorted(od.iteritems(), key=lambda d: d[1], reverse= True)
	for tag, num in tagdic.items():
		finallist= ','.join(tag) 
