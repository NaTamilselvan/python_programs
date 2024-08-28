
a=[1,2,3,4,5,6]

#a[1],a[3]=a[3],a[1]

#a[0],a[2]=a[2],a[0]

#print(a)

k=3

for i in range(k):
    
    tar=a[0]
    
    for j in range(len(a)-1):
        
        a[j]=a[j+1]
        
        
    a[len(a)-1]=tar




print(a)    