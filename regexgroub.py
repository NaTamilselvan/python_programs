import re

s="""tamilselvanme2810@gmail.com

     tamilinfotech26vkm@gmail.com
     
     tamilselvanselvi1028@gmail.com
     
     vltamilselvi2810@gmail.com
     
     tamil28-03_1998$@gmail.com

"""


regex=r"([a-zA-z0-9_$\-]+)@([a-zA_Z0-9]+.com)"

l=re.search(regex, s) 

print(l.group(0))

print(l.group(1))

print(l.group(2))


print(l)