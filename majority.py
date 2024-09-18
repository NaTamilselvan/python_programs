def majorityelemnt(a):
    
    m=a[0]
    i=1
    count=1
    while(i<len(a)):
       
        if count==0:
           count=+1
           m=a[i]
        elif m==a[i]:
            count+=1
        else :
            count-=1
            
        i+=1    
    print("The majaority element is ",m)
    
    
a=[22,22,3,1,22,3]

print(len(a)//2)

majorityelemnt(a)

    
    
            
            
      
    