import re

s="python is world most popular  high level programming language "

regex=r"[^aeiou]"

l=re.findall(regex, s)

print(l)
