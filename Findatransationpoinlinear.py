'''This program for daily Dose code io series daily one ok 
This is a first program

Given a sorted array containing only 0s and 1s, find the transition point, i.e., the first index where 1 was observed, and before that, only 0 was observed.

Example 1:

Input:
N = 5
arr[] = {0,0,0,1,1}
Output: 3
Explanation: index 3 is the transition 
point where 1 begins.

link:https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1

'''


def codeiosolution(l,n):
    
    begin=0
    end=n-1
    flag=0
    
    if len(l)==1 and l[0]==0:
        return -1
    
    while(begin<=end):
        
        
        mid=(begin+end)//2
        
        if a[mid]==1 and a[mid-1]==0:
             return mid
        elif a[mid]==1:
            flag=1
            end=mid-1
        else:
            begin=mid+1
            
            
    if flag==0:
          return -1   
    
    

def transaction(l,n):
    
    if len(l)==0:
        return 0
    
    else:
        postion=-1
        notOne=True
        
        for i in range(len(l)):
            
            if l[i]==1 and l[i-1]==0:
                
                postion=i
                notOne=False
                return postion
            
            
            
        if notOne:
            return -1
        
        
        
 
        
a=[0,0,0,0,0,1]
result=transaction(a, len(a))

print(result)
                


