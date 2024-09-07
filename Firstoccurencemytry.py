def firstrepeat(a):
    
    
    for i in range(len(a)):
        
        for j in range(i+1,len(a)):
            
            if a[i]==a[j] :
                # print("The first occurence is ",a[i])
                return a[i]
    
        
    return -1
    
    
a=[10, 5, 3, 4, 3, 5, 6]
l=firstrepeat(a)


if l== -1:
    print("The three is no repeating element")

else:
    print("The repeating element ",l)
        