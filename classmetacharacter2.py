import re

s="python is world most popular  A high level programming language 0998888887 "

regex=r"[a-z]"

regex=r"[A-Z]"

regex=r"[0-9]"


regex=r"[^a-z]"

regex=r"[^A-Z]"

regex=r"[^0-9]"


regex=r"[^a-zA-Z0-9]"

l=re.findall(regex, s)

print(l)
