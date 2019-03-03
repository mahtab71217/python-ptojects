# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:09:56 2019

@author: mahtab
"""

sen=input('Enter your sen: ')
upper=0
lower=0
new_sen=sen.split(' ')
for i in range(0,len(new_sen)):
    b=new_sen[i]
    for j in range(0,len(b)):
        if  b[j].isupper():
            upper=upper+1
        else:
            lower=lower+1
print('UPPER CASE',' ',upper,'\n', 'LOWER  CASE',' ',lower )
            
            