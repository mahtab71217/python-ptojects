# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:29:28 2019

@author: mahtab
"""
coun=[]
class counter():
    def numbers(self,n):
        for i in range(0,n):
            if i%7==0:
                coun.append(i)
        return coun
      
p=counter()
n= eval(input("Enter the number"))
p.numbers(n)




               