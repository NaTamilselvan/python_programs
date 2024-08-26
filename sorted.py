def sortedorder(a):
    
    length=len(a)
    
    for i in range(length):
        for j in range(i+1,length):
            
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                
                
                
                
                
    print(a)
    
    
    
    
a=[2,3,4.5,12,44,11,-5,2]
sortedorder(a)
