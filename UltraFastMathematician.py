# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:22:26 2024

@author: ASUS
"""
import sys
n1 = input()
n2 = input()
for i in range(0, len(n1)):
    if n1[i] == n2[i]:
        a = "0"
    else:
        a = "1"
    sys.stdout.write(a)
    sys.stdout.flush()