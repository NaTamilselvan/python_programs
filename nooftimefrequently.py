# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 00:03:03 2024

@author: ELCOT
"""

def nooofsequence(lst):
    print("hi")
    
    length=len(lst)
    len2=[None]*length
    print(len(len2))
    
    for i in range(length):
        key=lst[i]
        count=1
        for j in range (i+1,length):
            if lst[i]==lst[j]:
                count+=1
                len2[j]=-1     
                
        
        if(len2[i]!=-1):
            len2[i]=count
            
            
            
    for i in range(length):
          if len2[i]>0:
              print(lst[i],"occurence is ",len2[i])
              
              
    
              
lst=[10,20,30,40,50,60,70,10,20,30,40,50,60,70,10]    
nooofsequence(lst)    
              
              