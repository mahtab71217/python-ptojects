# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:04:55 2019

@author: mahtab faraji
www.onlinebme.com
"""
sen='hello'
all_sen=[]
k=0
while len(sen)!=0:
    sen=input('Enter your sentence: ')
    k=k+1
    all_sen.append(sen)

for i in range(len(all_sen)):
    print(all_sen[i])
    
for i in range(len(all_sen)):
    u=all_sen[i].upper()
    print(u)

