def factorial(n):
      if (n==1 or n==0):
         return 1
      else :
          fact=1
          for i in range(2,n+1) :
              fact*=i
              
          return fact    

        
def factorial2(n):

     return 1 if n==0 or n==1 else n*factorial2(n-1)

    
  


#The next program is factorial list 


def factoriallist(k):

     n=1
     while(n<=k):
         if (n==1 or n==0):
             print("1",end=" ")
         else :
             fact=1
             for i in range(2,n+1) :
                 fact*=i
                 
             print(fact,end=" ")    
         n+=1
         

       
#factoriallist(6)

#This program for prime :
    
def prime(n):
    
    bool=True
    
    if n==1 :
        bool=True
    else:   
    
        for i in range(2,n):
            
            if n%i==0:
                bool=False
                break
    
    
    if(bool==True):
         print("Its prime number")
    else:
         print("Its  not prime number")
    
    
    

#prime(11)

#This program for prime number list 

def primeNumberList(l):
     
    for i in range(1,l+1):
       #  print(i)
        if i==1 or i==2 :
            print(i," is a prime number" )
        else:
           for j in range (2,int(i/2)+1) :
            
               if (i%j==0):
                 print(i, "not a prime numner")
                 break
               else :
                 print( i," is prime ")


primeNumberList(12)        
    
    
    
    
    
    
    



