import urllib2
import json as js

def image_url(subject):
    sub_var =  subject
    url = urllib2.urlopen("http://www.astrobin.com/api/v1/image/?subjects=" + sub_var + "&limit=1&api_key=30e22a64907ba74a4e359a33d3e1b3ed9b443b7f&api_secret=afd5ef0d064df3e5574c032a5ab3af2e8028867e&format=json")
    info = url.read()
    params = js.loads(info)

    #print params['objects'][0]['url_hd']
    print info
    
    
