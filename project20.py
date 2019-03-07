# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:08:06 2019

@author: mahtab
"""
import math
point=[(0,0)]
dis_p=0
l=[]
while True :
    s=input('Enter your direction: ')
    if not s:
        break
    l.append(tuple(s.split(' ')))
for i in range(0,len(l)):
    if l[i][0]=='UP':
        point=[(point[0][0],eval(l[i][1])+point[0][1])]
        dis_p=l[i][1]
       #dis= math.sqrt((first_point[0][0]-0)+(first_point[0][1]-l[i][1]))
    if l[i][0]=='DOWN ':
        point=[(point[0][0],point[0][1]-l[i][1])]
        dis_p=l[i][1]
    if l[i][0]=='LEFT':
        point=[(point[0][0]-l[i][1],point[0][1])]
        dis_p=l[i][1]

    if l[i][0]=='RIGHT':
        point=[(point[0][0]+l[i][1]),point[0][1]]
        dis_p=l[i][1]

        


        
       

    
    

