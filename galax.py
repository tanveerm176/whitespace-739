import urllib2 
import json as js

def labels():
    galax_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/local_groups')
    galax_info = galax_url.read()
    galax_params = js.loads(galax_info)
    label= []
    
    for i in galax_params:
         label.append(i['label'])
    
    return label[:25]
    #return galax_params

def distly():
    galax_url = urllib2.urlopen('http://star-api.herokuapp.com/api/v1/local_groups')
    galax_info = galax_url.read()
    galax_params = js.loads(galax_info)
    distance = []
    
    for i in galax_params:
        distance.append(i['distly'])
    
    return distance[:25]
    




label_list = labels() 
dist_list = distly()
galax_dict = {}

def extract_dict():
    len_label = range(len(label_list))
    
    for x in len_label:
        galax_dict[label_list[x]]=(dist_list[x])
    
    return galax_dict

def select_galax(galaxy):
    return extract_dict()[galaxy]

