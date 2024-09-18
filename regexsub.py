import re

s="""tamilselvanme2810@gmail.com

     tamilinfotech26vkm@gmail.com
     
     tamilselvanselvi1028tt@gmail.com
     
     vltamilselvi2810@gmail.com
     
     tamil28-03_1998$@gmail.com

"""


regex=r"@gmail.com"

l=re.findall(regex, s)

s=re.sub(regex,"@yahoo.com",s)

print(s)

