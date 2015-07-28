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
def _text():
	u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?date="+date()+"&concept_tags=True&api_key=TCmI6MYSNZZB72Jk4x8iwHgGgCwQhyqbvKJ00rcV")
	xtextx = u.read()
	text = json.loads(xtextx)
	return text

def get_img():
	nasa_img = _text()['url']
	return nasa_img

	
def get_title():
	_title = _text()['title']
	return _title

def get_expl():
	expl = _text()['explanation']
	return expl
