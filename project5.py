# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:19:02 2018

@author: mahtab
"""

#project5
class onlinebme():
    def getString(self,strring_input):
        self.input=strring_input
        
        
    def printString(self):
        print(self.input)
        
        
p=onlinebme()
string=input('Enter the string: ')
out_1=p.getString(string)
out_2=p.printString()