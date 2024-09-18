import re

s="python is world most popular  high level programming language 77777775443333 "

regex=r"\w"

regex=r"\W"

regex=r"\D"

regex=r"\S"

l=re.findall(regex, s)

print(l)
