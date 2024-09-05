def bubble(a):
    
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1] :
                a[j+1],a[j]=a[j],a[j+1]
        
    
                  
                  
                  
                  
                  
                  
a=[22,2,5,2,5,7,1]

bubble(a)

print(a)                  
                  