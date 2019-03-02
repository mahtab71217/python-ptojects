# -*- coding: utf-8 -*-
"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Created on Thu Feb 28 22:53:16 2019

@author: mahtab faraji
www.onlinebme.com
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
       
       
       





            
    
       
           
  
           
           
          
     
          
     
            
    
