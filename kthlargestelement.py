def KthlargestLEment(a):
    
    length=len(a)
    
    for i in range(length):
         for j in range(i+1,length):
             if a[i]>a[j]:
                 
                 temp=a[i]
                 a[i]=a[j]
                 a[j]=temp
                 
                 
                 
                 
                 
u=[41,56,3,4,6,78,2,12]                
KthlargestLEment(u)

print(u)

print(u[5])