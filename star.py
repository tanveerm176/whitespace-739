import urllib2 
import json as js

def labels2():
    star_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/stars')
    star_info = star_url.read()
    star_params = js.loads(star_info)
    label= []
    
    for i in star_params:
         label.append(i['label'])
    
    return label[:25]
    #return star_params[:100]

def distly2():
    star_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/stars')
    star_info = star_url.read()
    star_params = js.loads(star_info)
    distance = []
    
    for i in star_params:
        distance.append(i['distly'])
    
    return distance[:25]
    




label_list = labels2() 
dist_list = distly2()
star_dict = {}

def extract_dict():
    print type(label_list[0])
    len_label = range(len(label_list))
    
    for x in len_label:
        star_dict[label_list[x]]=dist_list[x]
    
    return star_dict

def select_star(star):
    return extract_dict()[star]

