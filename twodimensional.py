import math

def squr(f):
    
    s=int(math.sqrt(f))
    return  s*s==f


def given_num_check(n):
    
       return squr(5*n*n+4) or  squr(5*n*n-4)
     
    
    
def nthmultiple (k,n):

    f,s,t,i=0,1,0,2
    
    
    while(i!=0):
        
        t=f+s
        #print(f,end=" ")
        
        f=s
        
        s=t
        
        if s%k==0:
            return i*n
        
        i+=1
        
        
        
       


def given_number_fibbo(n):
    
    
    a,b=1,1
    c=0
    while(c<n):
        
        c=a+b
         
        a=b
        
        b=c
        
        
        
    if c==n:
        print("The number is fibbo")
        
    else:
        print("The number is not fibbo")



def fibonumber(n):
    
    
    "This program for fibbonaci number "
    
    
    f,s,t,i=0,1,0,0
    
    
    while(i<=n):
        
        t=f+s
        print(f,end=" ")
        
        f=s
        
        s=t
        
        i+=1
        
        
        
        
        
        
        
#fibonumber(10)

given_number_fibbo(8)


n=int(input("Enter the number\n"))

if given_num_check(n) == True:
     print("fibbo number ")
else :
      print("not fibbbo")
     
        
     
        
     
print(nthmultiple(2,9))        