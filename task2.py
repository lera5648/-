#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

s=sys.argv[1:3]
with open("%s" %s[0]) as file:
    array = [row.strip() for row in file]
f1 = [i for line in array for i in line.split()]

x_center=int(f1[0])
y_center=int(f1[1])
r=int(f1[2])

with open("%s" %s[1]) as file:
    array = [row.strip() for row in file]
f2 = [i for line in array for i in line.split()]
f2 = list(map(int, f2))
x=[]
y=[]

for i in range(0, len(f2)):
    if(i%2==0):
        x.append(f2[i])
    else:
        y.append(f2[i])

        
for i in range(0,len(x)):
    if((x[i]-x_center)**2+(y[i]-y_center)**2<r**2):
        print(1)
    if((x[i]-x_center)**2+(y[i]-y_center)**2==r**2):
        print(0)
    if((x[i]-x_center)**2+(y[i]-y_center)**2>r**2):
        print(2)

