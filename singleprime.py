def givennumberprime(n):
    
    for i in range(2,int(n//2)+1):
        
        if n % i ==0:
            print("The number is not prime")
            break
        
        
    else :
         print("The number n is prime ",n)
         
         
         
         



n=6

givennumberprime(n)         