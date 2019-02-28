#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010
#Created on Thu Feb 28 22:17:31 2019

#@author: mahtab faraji
#www.onlinebme.com
"""

sen=input('Enter your sentence: ')
new_sen=sen.split(',')
for i in range(0,len( new_sen)):
    summ=0
    char=new_sen[i]
    for j in range(0,len(char)):
        summ=summ+eval(char[j])*(2**j)
    if summ%5==0:
        print(new_sen[i])





        
    
