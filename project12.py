# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:53:16 2019

@author: mahtab
"""
out=[]
for i in range(1000,3001):
    res=[]
    num=str(i)
    for j in range(0,4):
        b=eval(num[j])%2
        res.append(b)
    if sum(res)==0:
       out.append(str(i))
       
       
       
main_out = ''.join(out)
       
       
       





            
    
       
           
  
           
           
          
     
          
     
            
    