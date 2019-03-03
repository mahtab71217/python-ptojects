# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:37:05 2019

@author: mahtab
"""

seq=input('Enter the sequence of numbers: ')
new_seq=seq.split(',')
out=[]
for i in range(0,len(new_seq)):
    if eval(new_seq[i])%2 !=0:
        out.append((new_seq[i]))
print( ' ,'.join(out))
        