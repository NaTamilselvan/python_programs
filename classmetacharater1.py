
import re

s="Hi today every place is computer and most important programming language  Hi"

regex=r"[aeiou]"

#regex=r"hi$"


m=re.findall(regex, s)

print(m)

