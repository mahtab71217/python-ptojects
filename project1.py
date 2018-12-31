# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:20:58 2018

@author: mahtab
"""
#project1
out=[]
for i in range(2000,3201):
    if i%7==0 and (i%5!=0):
            out.append(i)
            
print(out)