lst =[12,33,44,6,8,9,1,3,4]

lst2=[23,1,3,6,4]

union=[]

intersection=[]

l1=len(lst)

l2=len(lst2)

length=0
length2=0

if l1>l2:
    length=l1
    length2=l2
else:
    length=l2 
    length2=l1

for i in range(length):
     for j in range(length2):
         if(lst[i]==lst2[j]):
             union.append(lst[i])
             break
     else:
          intersection.append(lst[i])
    
    
    
print(union)
print(intersection)    
    
    