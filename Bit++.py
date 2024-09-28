# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:53:49 2024

@author: ASUS
"""
n = int(input())
ans = 0
for i in range(0, n):
    s = input()
    if((s == "++X") | (s == "X++")):
       ans += 1
    elif((s == "--X") | (s == "X--")):
       ans -= 1
print(ans)