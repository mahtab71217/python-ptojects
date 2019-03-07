# -*- coding: utf-8 -*-
"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Created on Thu Mar  7 16:08:06 2019

@author: mahtab faraji
www.onlinebme.com""
import math
point=[(0,0)]
dis_p=0
l=[]
while True :
    s=input('Enter your direction: ')
    if not s:
        break
    l.append(tuple(s.split(' ')))
for i in range(0,len(l)):
    if l[i][0]=='UP':
        point=[(point[0][0],eval(l[i][1])+point[0][1])]
        dis_p=l[i][1]
       #dis= math.sqrt((first_point[0][0]-0)+(first_point[0][1]-l[i][1]))
    if l[i][0]=='DOWN ':
        point=[(point[0][0],point[0][1]-l[i][1])]
        dis_p=l[i][1]
    if l[i][0]=='LEFT':
        point=[(point[0][0]-l[i][1],point[0][1])]
        dis_p=l[i][1]

    if l[i][0]=='RIGHT':
        point=[(point[0][0]+l[i][1]),point[0][1]]
        dis_p=l[i][1]

        


        
       

    
    

