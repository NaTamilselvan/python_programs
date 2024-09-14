#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:43:35 2024

@author: natamilme
"""

a=[10,0,20,30,4,3,2]

a[1:]=[3,2,4,44,4,3]

print(a)


a.insert(0, 11)

print(a)


lst=[10,20,30,40,50,4,4]

lst[::2]=["00","00","00","00"]

print(lst)


lst.remove("00")

print(lst)

while "00" in lst:
    lst.remove("00")
    
    
    
print(lst)    

