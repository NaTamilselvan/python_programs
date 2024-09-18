def fun(s):
    s=s.split()

re=[]
    re=[re.append(i)    i.upper() if len(i)>5 else i.lower()              for i in s:     ] 
    
    

    
    
    

a="hi welcome python progras"


a=a.split()

print(a)

re=[]

for i in a:
    
    if len(i)>5:
       re.append(i.upper())
       
       
    elif len(i)<=5 :
        re.append(i.lower())
        
        
        
print(" ".join(re))       