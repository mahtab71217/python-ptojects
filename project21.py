# -*- coding: utf-8 -*-
"""Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Created on Thu Mar  7 19:36:49 2019

@author: mahtab faraji
www.onlinebme.com
""
from string import Template
sen=input("Enter your sentence: ")
new_sen=sen.split(' ')
out=[]
b=[]
a=[]
for i in range(len(new_sen)):
    #out.append(new_sen.count(new_sen[i]))
    b=new_sen.count(new_sen[i])
    print(new_sen[i],':',b)
    
#out_m=list(zip(a,b,out))
#o=[]
#for i in range(0,len(out_m)):
 #   ' '.join(list(out_m[i]))
    

#count=len(new_sen)  
#while count==0:
    #print(a[i],b[i],out[i])
    #count=count-1
#for i in new_sen:
    #print(b "%s:%d" % (new_sen[i],out[w])
    
