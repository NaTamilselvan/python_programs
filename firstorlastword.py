import re 

s="python is one the most popular programming langauge python"

refex=r"^python"

refex=r"python$"

   
match=re.search(refex, s)

print(match)