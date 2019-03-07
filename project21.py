# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:36:49 2019

@author: mahtab
"""
from string import Template
sen=input("Enter your sentence: ")
new_sen=sen.split(' ')
out=[]
b=[]
a=[]
for i in range(len(new_sen)):
    #out.append(new_sen.count(new_sen[i]))
    b=new_sen.count(new_sen[i])
    print(new_sen[i],':',b)
    
#out_m=list(zip(a,b,out))
#o=[]
#for i in range(0,len(out_m)):
 #   ' '.join(list(out_m[i]))
    

#count=len(new_sen)  
#while count==0:
    #print(a[i],b[i],out[i])
    #count=count-1
#for i in new_sen:
    #print(b "%s:%d" % (new_sen[i],out[w])
    