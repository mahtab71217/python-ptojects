#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:00:17 2019

@author: mahtab
www.onlinebme.com
"""
sen=input('Enter your sentence: ')
new_sen=sen.split(' ')
for i in range(len(new_sen)):
     b=new_sen.count(new_sen[i])
     if b>=2:
        ind=new_sen.index(new_sen[i])
        new_sen[ind]='double'
new_sen.remove('double')
b=', '.join(new_sen)
newstr = b.replace(",", " ")

         
         
         
    
