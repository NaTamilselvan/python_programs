s="{{(})}}"
lst=[]

for i in s:
    
    if i=='[' or i=='{' or i=='(' :
    
        lst.append(i)
        
    elif i=='}' and lst[-1]=='{' :
     
         lst.pop()
         
    elif i==']' and lst[-1]=='[':
     
         lst.pop()
         
    elif i==')' and lst[-1]=='(':
     
         lst.pop()   
    else :
         break
     
        
     
print(lst)


if len(lst)==0:
    print("ok")
    
else:
    print("not ok ")    
       