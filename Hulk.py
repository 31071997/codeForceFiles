# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 03:12:54 2024

@author: ASUS
"""
def LoveHate(f):
    if(f == False):
        word = "hate"
        f = True
    elif(f == True):
        word = "love"
        f = False
    print( "I "+ word, end=" ")
first = True
n = int(input())
while(n > 0):
    first = not first
    LoveHate(first)
    if(n == 1):
        print("it", end=" ")
    else:
        print("that", end=" ")
    n -= 1