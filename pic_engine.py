import json
import urllib2
import random

def date():
	a = str(random.randint(1997,2014))
	b = str(random.randint(1,12))
	if len(b) == 1:
		b = "0" + b
	c = str(random.randint(1,29))
	if len(c) == 1:
		c = "0" + c
	date = a + "-" + b +"-" + c
	return date

u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?date="+date()+"&concept_tags=True&api_key=DEMO_KEY")
xtextx = u.read()
text = json.loads(xtextx)

def get_img():
	nasa_img = text['url']
	return nasa_img

	
def get_title():
	_title = text['title']
	return _title

