

def rotateArray(a,n):
    
    l=len(a)
    
    b=[None]*l
    k=1
    while(k<=n):
      for i in range(l):
           b[(i+n)%l]=a[i]
      k+=1  
    print(b)    
        
a=[12,33,4,53,2,7,8,2]
n=2

rotateArray(a, n)       

        
        
        
    
    