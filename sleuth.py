# -*- coding: utf-8 -*-
"""
Created on Mon May 20 02:20:53 2024

@author: ASUS
"""

a = input()
if(a[len(a)-1] == '?'):
    i= len(a)-2
    while(i >= 0):
        if(a[i] == 'a' or a[i] == 'b' or a[i] == 'c' or a[i] == 'd' or a[i] == 'e' or a[i] == 'f' or a[i] == 'g' or a[i] == 'h' or a[i] == 'i' or a[i] == 'j' or a[i] == 'k' or a[i] == 'l' or a[i] == 'm' or a[i] == 'n' or a[i] == 'o' or a[i] == 'p' or a[i] == 'q' or a[i] == 'r' or a[i] == ' s' or a[i] == 't' or a[i] == 'u' or a[i] == 'v' or a[i] == 'w' or a[i] == 'x' or a[i] == 'y' or a[i] == 'z' or a[i] == 'A' or a[i] == 'B' or a[i] == 'C' or a[i] == 'D' or a[i] == 'E' or a[i] == 'F' or a[i] == 'I' or a[i] == 'J' or a[i] == 'K' or a[i] == 'L' or a[i] == 'M' or a[i] == 'N' or a[i] == 'O' or a[i] == 'P' or a[i] == 'Q' or a[i] == 'R' or a[i] == 'S' or a[i] == 'T' or a[i] == 'U' or a[i] == 'V' or a[i] == 'W' or a[i] == 'X' or a[i] == 'Y' or a[i] == 'Z'):
            if(a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' or a[i] == 'y' or a[i] == 'A' or a[i] == 'E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U' or a[i] == 'Y'):
                print("YES")
                break
            else:
                print("NO")
                break
        else:
            i-=1