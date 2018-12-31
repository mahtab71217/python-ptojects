# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:27:11 2018

@author: mahtab
"""

#project6
import math
c=50
H=30
out=[]
D=list(eval(input('Enter the sequance of D values: ')))
for i in D:
    o=round(math.sqrt((2*c*i)/H))
    out.append(o)
print(out)
