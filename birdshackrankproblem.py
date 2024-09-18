l=[1,2,1,2,1,2,3,4,3,4,2,1,5
   ]

birds=[0]*len(l)


for i in range(len(l)):
    
    k=l[i]
    
    if birds[k]==None:
        birds[k]=1
    else:
        r=birds[k]
        birds[k]=r+1
        
        
        
        
print(birds)




index=0
max=birds[0]
for i in range(len(birds)):
    
    if birds[i]>max:
        max=birds[i]
        index=i
       
        
       
print("The max is index is ",index,"max value ",max)
        