#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:55:59 2024

@author: natamilme
"""

strr=[10,20,30,40,50]

#print(strr[1::2])

start=0
end=len(strr)-1

while start<end:
      
       strr[start],strr[end]=strr[end],strr[start]
       start+=1
       end-=1
       
       
       
print(strr)       