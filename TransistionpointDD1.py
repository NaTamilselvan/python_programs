def D1transistionpoint(a):
    
    start=0
    end=len(a)-1
    flag=0
    
    while(start <= end):
        
        if len(a)==1 and a[0]==0:
            return -1
        
        mid=(start+end)//2
        
        
        
        if (a[mid]==1 and a[mid-1]==0) :
            return mid
        
        elif a[mid]==1:
             end=mid-1
             flag=1
             
        else:
            start=mid+1
        
        
    if flag==0:
        return -1
    
    
    
    
a=[0,0,0,0,0,1,1]    

k=D1transistionpoint(a)
 
print("The trasisition point",k)
   
    