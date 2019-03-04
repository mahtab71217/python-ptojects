# -*- coding: utf-8 -*-
"""A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Created on Mon Mar  4 15:46:01 2019

@author: mahtab faraji
www.onlinebme.com
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
    
         
