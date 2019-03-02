# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:41:32 2019

@author: mahtab
"""

sen=input('Enter your sen: ')
new_sen=sen.split(' ')
digit=0
letter=0
for i in range(0,len(new_sen)):
    a=new_sen[i]
    for j in range(0,len(a)):
        asci=ord(a[j])
        if (asci>= 97 and asci <= 122) or (asci >= 65 and asci <= 99):
            letter=letter+1
        else:
            digit=digit+1
print('LETTERS ',' ',letter,'\n', 'DIGITS ',' ', digit)            
            
            


            

