#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:08:59 2024

@author: natamilme
"""

lst=[1,2,0,17,2,0,1,2,0]


length=len(lst)


for i in range(length):
    
     for j in range(i+1,length):
         
         if lst[i]>lst[j] :
             temp =lst[i]
             lst[i]=lst[j]
             lst[j]=temp
             
             
print(lst)             
             