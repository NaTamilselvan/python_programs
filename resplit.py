import re

s="28:03:1998"


l=re.split(r"[-:]", s)

date,month,year=l

print(date,month,year)