# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:34:40 2024

@author: ASUS
"""
a, b = input().split()
a = int(a)
b = int(b)
ans = []
if(a < b):
    ans.append(a)
    c = b-a
    if(c >= 2):
        ans.append(int(c/2))
    else:
        ans.append(0)
else:
    ans.append(b)
    c = a-b
    if(c >= 2):
        ans.append(int(c/2))
    else:
        ans.append(0)
print(str(ans[0])+" "+str(ans[1]))