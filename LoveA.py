# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 01:39:05 2024

@author: ASUS
""" 
s = input()
l1 = len(s)
l2 = s.count('a')
if(l2 > (l1/2)):
    print(l1)
else:
    print((2 * l2) - 1)