def common_e_Array(a,b,d):
    
    c={}
    
    for i in a:
        c[i]=1
        
    for j in b:
        
        if j in c and c[j]==1 :
            
            c[j]=2
            
    for k in d:
         if k in c and c[k]==2:
   
             c[k]=3
             
             
             
    li=[]       
    for key,value in sorted(c.items()):
            
        if value==3 :
           li.append(key) 
        
        
    return li







a=[2,3,4,5,6,7]
b=[5,6,7,8,9]
c=[7,8,9]     
         
ll=common_e_Array(a,b,c)
print(ll)