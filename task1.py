#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mas(n,m):
    km=[]
    k=0
    s=0
    i=0
    j=0 #счетсчик m
    while(True):
        
        k=k+1
        if(j%m==0):
            km.append([])
            i=0
        if(j==0):
            km[j//m].append(1)
        elif(j%m==0 and j!=0):
            km[j//m].append(km[j//m-1][-1])
        elif(j%m!=0):
            s=km[j//m][i]+1
            if(s==n+1):
                s=1
            i=i+1
            km[j//m].append(s)
            
        if(len(km[j//m])==m):
            if(km[j//m][m-1]==1):
                break

        j=j+1
        
       
    return km


import sys

s=sys.argv


#s=s.split(' ')
s=s[1:3]
s=list(map(int, s))
#len(mas(s[0],s[1]))
for i in range(0, len(mas(s[0],s[1]))):
    print(mas(s[0],s[1])[i][0])
            


# In[ ]:




