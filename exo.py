import urllib2 
import json as js

def labels():
    exo_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/exo_planets')
    exo_info = exo_url.read()
    exo_params = js.loads(exo_info)
    label= []
    
    for i in exo_params:
         label.append(i['label'])
    
    return label[:25]
    #return exo_params[:50]

def distly():
    exo_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/exo_planets')
    exo_info = exo_url.read()
    exo_params = js.loads(exo_info)
    distance = []
    
    for i in exo_params:
        distance.append(i['distance'])
    
    return distance[:25]
    




label_list = labels() 
dist_list = distly()
exo_dict = {}

def extract_dict():
    print type(label_list[0])
    len_label = range(len(label_list))
    
    for x in len_label:
        exo_dict[label_list[x]]=dist_list[x]
    
    return exo_dict




def select_exo(exo):
    return extract_dict()[exo]


