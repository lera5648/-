#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

s=sys.argv[1]

with open(s) as file:
    array = [line.rstrip() for line in file]
array=list(map(int,array))
print(sum(abs(v - sorted(array)[len(array) // 2]) for v in array))

