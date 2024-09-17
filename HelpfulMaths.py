# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 01:14:26 2024

@author: ASUS
"""
s = input().split("+")
a = list(s)
n = len(a)
ans = []
string = ""
for i in range(0, n):
    a[i] = int(a[i])
a.sort()
for i in range(0, n):
    if(i != (n-1)):
        ans.append(str(a[i])+"+")
    else:
        ans.append(str(a[i]))
for i in range(0, n):
    string += str(ans[i]) 
print(string)