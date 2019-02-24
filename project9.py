#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT
#Created on Sat Feb 23 18:04:55 2019

@author: mahtab faraji
www.onlinebme.com
"""
sen='hello'
all_sen=[]
k=0
while len(sen)!=0:
    sen=input('Enter your sentence: ')
    k=k+1
    all_sen.append(sen)

for i in range(len(all_sen)):
    print(all_sen[i])
    
for i in range(len(all_sen)):
    u=all_sen[i].upper()
    print(u)

