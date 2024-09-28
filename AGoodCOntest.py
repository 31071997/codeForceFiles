# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:32:32 2024

@author: ASUS
"""
ans = ""
p = []
n = int(input())
for i in range(0, n):
    p = input().split()
    if((int(p[1]) >= 2400) & (int(p[2]) > int(p[1])) & (ans != "YES")):
        ans = "YES"
if(ans != "YES"):
    ans ="NO"
print(ans)  