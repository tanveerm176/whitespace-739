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
        list_text = []
        a = list_text.append(text)
        return list_text

if _text()[0]['media_type'] == 'image':
        def get_img():
                date_text = _text()
                nasa_img = date_text[0]['url']
                _title = date_text[0]['title']
                expl = date_text[0]['explanation']
        
                # return nasa_img,_title,expl
                return nasa_img, _title , expl 
