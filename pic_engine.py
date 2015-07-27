import json
import urllib2
import random

def date():
	a = str(random.randint(1997,2014))
	b = str(random.randint(1,12))
	if len(b) == 1:
		b = "0" + b
	c = str(random.randint(1,30))
	if len(c) == 1:
		c = "0" + c
	date = a + "-" + b +"-" + c
	return date



print a
print b
print c

def get_img():
	u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?date="+date()+"&concept_tags=True&api_key=DEMO_KEY")
	xtextx = u.read()
	text = json.loads(xtextx)
	nasa_img = text['url']
	return nasa_img

	
#def get_title():
#	q = urllib2.urlopen("https://api.nasa.gov/planetary/apod?date="+a+"-"+b+"-"+c+"06&concept_tags=True&api_key=DEMO_KEY")
#	xxtextxx = u.read()
#	xxxtextxxx = json.loads(xxtextxx)
#	_title = xxxtextxxx['title']
#	return _title

