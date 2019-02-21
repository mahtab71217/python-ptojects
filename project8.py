# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:16:09 2019

@author: mahtab faraji
www.onlinebme.com
"""
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

x=input('Enter the first number: ')
my_list=x.split(',')
sort_list=sorted(my_list)
new_str=','.join(sort_list)
print(new_str)
