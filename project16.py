# -*- coding: utf-8 -*-
"""Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Created on Sun Mar  3 11:37:05 2019

@author: mahtab faraji
www.onlinebme.com
"""

seq=input('Enter the sequence of numbers: ')
new_seq=seq.split(',')
out=[]
for i in range(0,len(new_seq)):
    if eval(new_seq[i])%2 !=0:
        out.append((new_seq[i]))
print( ' ,'.join(out))
        
