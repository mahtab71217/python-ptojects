# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:30:56 2019

@author: mahtab faraji
www.onlinebme.com

"""
#Question: 
#Write a program which takes 2 digits, X,Y as input and 
#generates a 2-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

#answer: 
import numpy as np
x=eval(input('Enter the first number: '))
y=eval(input('Enter the second number: '))

my_array=np.ones((x,y))
for i in range(x):
    for j in range(y):
        my_array[i,j]=i*j
        
        
        
        
      
    

