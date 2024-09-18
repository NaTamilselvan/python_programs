import re

s="teeth  week are very  weak important is tooth teeth "

regex=r"[aeiou]{2}"


regex=r"we[ae]k"


l=re.findall(regex, s)

print(l)
