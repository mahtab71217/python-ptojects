# -*- coding: utf-8 -*-
"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
Created on Sun Mar  3 11:20:39 2019

@author: mahtab faraji
www.onlinebme.com
"""

a=input('Enter the value as a: ')

out=eval(a)+eval(a+a)+eval(a+a+a)+eval(a+a+a+a)
print(out)
    
    
