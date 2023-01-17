#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
def fill_json(json1, json2):
    for i in json1:
        for v in json2['values']:
            if i.get('id') == v.get('id'):
                i['value'] = v.get('value')
                break
        if 'values' in i.keys():
            fill_json(i['values'], json2)
    return json1

import sys

s=sys.argv[1:3]
            
f1 = open(s[0])
f2 = open(s[1])
# returns JSON object as 
# a dictionary
d1 = json.load(f1) 
d2 = json.load(f2)
fill_json(d1['tests'],d2)

