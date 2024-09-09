import re
s="""xyz12@gmil.cin

    abc@gmail.com
    
    Tamil28_10$@gmail.com
    
    tamilselvan1028@gmail.com
    
    tamilselvan1028@yahoo.com
    
    tamil_$-@gmail.com"""
    
    
    
regex=r"^[a-zA_Z0-9$_\-]+@gmail.com"

regex=r"[a-z0-9A-Z$_\-]+@[a-z\.]+.com"

l=re.findall(regex, s)

print(l)
 
   








    