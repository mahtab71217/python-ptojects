# -*- coding: utf-8 -*-
"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Created on Sun Mar  3 11:09:56 2019

@author: mahtab faraji
www.onlinebme.com
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
            
            
