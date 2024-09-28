# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:40:31 2024

@author: ASUS
"""
k , r = input().split()
k = int(k)
r = int(r)
i = 1
while(i != 0):
    increment = k*i
    if(((increment-r)%10 == 0) | (increment%10 == 0)):
        break
    i += 1
print(i)