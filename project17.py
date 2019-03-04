# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:46:01 2019

@author: mahtab
"""

password=input('Enter your password: ')
out=[]
password=password.split(',')
for i in range(0,len(password)):
    if len(password[i])>=6 and len(password[i])<=12:
        if (not(password[i].islower())) and (not(password[i].isupper())): 
           if any(i.isdigit() for i in password[i]):
               if ('$' in password[i]) or ('#' in password[i]) or ('@' in password[i]):
                  out.append(password[i])
    
         