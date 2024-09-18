import re

s="""tamilselvanme2810@gmail.com

     tamilinfotech26vkm@gmail.com
     
     tamilselvanselvi1028@gmail.com
     
     vltamilselvi2810@gmail.com
     
     tamil28-03_1998$@gmail.com

"""


regex=r"([a-zA-z0-9_$\-]+)@([a-zA_Z0-9]+.com)"

#l=re.finditer(regex, s) 

l=re.finditer(regex, s)


for m in l:
    
  # print(m)
   print(m.group(0))

   print(m.group(1))

   print(m.group(2))

   print()
#print(l)