def findDuplicate(d):
    
    for i in  range(len(d)):
        
        for j in range(i+1,len(d)):
            
            if d[i]==d[j]:
                print("The duplicate element",d[i])
                
                
                
                
                
                

a=[1,2,3,4,5,5,1]
findDuplicate(a)                