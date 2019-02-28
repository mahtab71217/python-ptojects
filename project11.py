# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:17:31 2019

@author: mahtab
"""

sen=input('Enter your sentence: ')
new_sen=sen.split(',')
for i in range(0,len( new_sen)):
    summ=0
    char=new_sen[i]
    for j in range(0,len(char)):
        summ=summ+eval(char[j])*(2**j)
    if summ%5==0:
        print(new_sen[i])





        
    