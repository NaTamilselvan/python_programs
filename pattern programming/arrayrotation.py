''' This program for array roatation'''

def rotate(l,n,r):
    ''' This program for array roatation'''    
    b=[0]*n
    
    for i in range(len(l)):
        b[(i+r)%n]=l[i]
        #print(f"The {a[i]} postion is ",postion)
    print(l)   
    print(b)

a=[1,2,3,45,5,6,7]

rotate(a,len(a),1)


size=len(a)



print(a)
start=a[0]
for i in range(1,len(a)):
    
    a[i-1]=a[i]
    
a[len(a)-1]=start 

print(a)
   
    
    
  
    
