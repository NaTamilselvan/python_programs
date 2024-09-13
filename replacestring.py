import re


s="Hi i am python developer"

redex=r"am"

k=re.sub(redex,"", s)


print(k)


print(len(s))

print(len(k))