# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:28:32 2024

@author: ASUS
"""
n = int(input())
nm = cm = 0
for i in range(0, n):
    m, c = input().split()
    m = int(m)
    c = int(c)
    if(m > c):
        nm += 1
    elif(m < c):
        cm += 1
if(nm > cm):
    print("Mishka")
elif(nm < cm):
    print("Chris")
else:
    print("Friendship is magic!^^")