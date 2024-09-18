import re

s="Hitamil i am python developer"

regex=r"[a-zA-z]+$"

d=re.findall(regex, s)

print(d)
