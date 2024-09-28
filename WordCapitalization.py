# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:47:13 2024

@author: ASUS
"""
s = input()
a = []
a = list(s)
string = ""
l = len(s)
if((a[0] != 'Z') & (a[0] != 'Y') & (a[0] != 'X') & (a[0] != 'W') & (a[0] != 'V') & (a[0] != 'U') & (a[0] != 'T') & (a[0] != 'S') & (a[0] != 'R') & (a[0] != 'Q') & (a[0] != 'P') & (a[0] != 'O') & (a[0] != 'N') & (a[0] != 'M') & (a[0] != 'L') & (a[0] != 'K') & (a[0] != 'J') & (a[0] != 'I') & (a[0] != 'H') & (a[0] != 'G') & (a[0] != 'F') & (a[0] != 'E') & (a[0] != 'D') & (a[0] != 'C') & (a[0] != 'B') & (a[0] != 'A')):
    a[0] = a[0].upper()
for i in range(0, l):
    string += a[i]
print(string)